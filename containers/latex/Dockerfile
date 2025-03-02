##
# Inspired by https://github.com/qdm12/latexdevcontainer
##

#checkov:skip=CKV_DOCKER_2: No healthcheck needed
#checkov:skip=CKV_DOCKER_3: User handled by devcontainer

# Build chktex for use in final stage
FROM mcr.microsoft.com/devcontainers/base:bookworm AS chktex_build
ARG CHKTEX_VERSION=1.7.8
ENV CHKTEX_FILE=chktex-${CHKTEX_VERSION}.tar.gz
ENV CHKTEX_URL=http://download.savannah.gnu.org/releases/chktex/${CHKTEX_FILE}
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/local/src
# hadolint ignore=DL3003
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential=12.9 \
 && curl -sSLO "${CHKTEX_URL}" \
 && tar -xzf "${CHKTEX_FILE}" \
 && cd "chktex-${CHKTEX_VERSION}" \
 && ./configure \
 && make \
 && mv chktex /usr/local/bin

# Functional stage
FROM mcr.microsoft.com/devcontainers/base:bookworm AS functional
SHELL ["/bin/bash", "-o", "pipefail", "-e", "-c"]
ENV SHELL=/bin/bash
ENV DEBIAN_FRONTEND=noninteractive

# Install texlive
ARG TEXLIVE_VERSION=2024
ARG TEXLIVE_MIRROR=http://ctan.math.illinois.edu/systems/texlive/tlnet
ARG TEXLIVE_INSTALL_NO_CONTEXT_CACHE=1
ARG TEXLIVE_INSTALL_NO_WELCOME=1

COPY "texlive-profile.txt" "/usr/local/src/texlive-profile.txt"
WORKDIR /usr/local/src
# hadolint ignore=DL3003
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential=12.9 \
        wget=1.21.3-1+b2 \
        gnupg=2.2.40-1.1 \
        cpanminus=1.7046-1 \
        bash-completion=1:2.11-6 \
 && curl -sSLO ${TEXLIVE_MIRROR}/install-tl-unx.tar.gz \
 && tar -xzf install-tl-unx.tar.gz \
 && rm install-tl-unx.tar.gz \
 && cd install-tl-* \
 && perl install-tl -profile /usr/local/src/texlive-profile.txt --location ${TEXLIVE_MIRROR} \
 && apt-get autoremove --purge -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && find /var/cache/apt -type f -print0 | xargs -0 rm -f

# Setup PATH
ENV PATH ${PATH}:/usr/local/texlive/${TEXLIVE_VERSION}/bin/x86_64-linux

# Latexindent dependencies
RUN cpanm -n -q Log::Log4perl \
 && cpanm -n -q XString \
 && cpanm -n -q Log::Dispatch::File \
 && cpanm -n -q YAML::Tiny \
 && cpanm -n -q File::HomeDir \
 && cpanm -n -q Unicode::GCString

RUN tlmgr install \
        latexindent \
        latexmk \
 && texhash \
 && rm /usr/local/texlive/${TEXLIVE_VERSION}/texmf-var/web2c/*.log \
 && rm /usr/local/texlive/${TEXLIVE_VERSION}/tlpkg/texlive.tlpdb.main.*

COPY --from=chktex_build /usr/local/bin/chktex /usr/local/bin/chktex

# Testing stage - verify binaries work and have the right permissions
FROM functional AS testing
RUN tlmgr version \
 && latexmk -version \
 && texhash --version \
 && chktex --version

# Final stage
FROM functional AS final
