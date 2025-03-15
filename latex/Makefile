# SPDX-License-Identifier: MIT
# Origin: https://github.com/thomvaill/tads-boilerplate

# Preserve intermediate files
.SECONDARY:

CV := cv
RESUMES := devops-engineer platform-engineer sre

DOCUMENTS := $(CV) $(RESUMES)

../pdf/cv.pdf: documents/cv.tex education/cv.tex experience/cv.tex skills/cv.tex summary/cv.tex
	cd documents && \
		xelatex -jobname cv -interaction=nonstopmode -output-directory=../../pdf cv.tex

education/cv.tex: templates/education.tex.j2 data/cv.yml data/common.yml data/education.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

experience/cv.tex: templates/experience.tex.j2 data/cv.yml data/common.yml data/experience.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

skills/cv.tex: templates/skills.tex.j2 data/cv.yml data/common.yml data/skills.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

summary/cv.tex: templates/summary.tex.j2 data/cv.yml data/common.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

../pdf/%.pdf: documents/%.tex education/%.tex experience/%.tex skills/%.tex summary/%.tex
	cd documents && \
		xelatex -jobname $* -interaction=nonstopmode -output-directory=../../pdf $*.tex

education/%.tex: templates/education.tex.j2 data/resume/%.yml data/common.yml data/education.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

experience/%.tex: templates/experience.tex.j2 data/resume/%.yml data/common.yml data/experience.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

skills/%.tex: templates/skills.tex.j2 data/resume/%.yml data/common.yml data/skills.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

summary/%.tex: templates/summary.tex.j2 data/resume/%.yml data/common.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

documents/%.tex: templates/resume.tex.j2 data/resume/%.yml data/common.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

documents/cv.tex: templates/cv.tex.j2 data/cv.yml data/common.yml
	@python3 render.py $< $@ $(filter-out $<, $^)

.PHONY: tex tex-documents tex-resumes tex-cv tex-education tex-experience tex-skills tex-summary

#:## Jinja-to-Tex Rendering
tex: tex-documents tex-education tex-experience tex-skills tex-summary ## Render all Jinja2 templates to Tex files
tex-documents: documents/$(DOCUMENTS).tex ## Render all documents
tex-resumes: documents/$(RESUMES).tex ## Render all resumes
tex-cv: documents/cv.tex ## Render the CV
tex-education: education/$(DOCUMENTS).tex ## Render all education
tex-experience: experience/$(DOCUMENTS).tex ## Render all experiences
tex-skills: skills/$(DOCUMENTS).tex ## Render all skills
tex-summary: summary/$(DOCUMENTS).tex ## Render all summaries

.PHONY: $(DOCUMENTS)

#:## Document Targets
devops-engineer: ../pdf/devops-engineer.pdf ## DevOps Engineer Resume
platform-engineer: ../pdf/platform-engineer.pdf ## Platform Engineer Resume
sre: ../pdf/sre.pdf ## Site Reliability Engineer Resume
cv: ../pdf/cv.pdf ## CV

.PHONY: clean clean-pdf clean-tex clean-documents clean-education clean-experience clean-skills clean-summary

#:## Clean
clean: clean-pdf clean-tex ## Clean all generated files
clean-pdf: ## Clean all PDFs
	@rm -f ../pdf/*.pdf ../pdf/*.log ../pdf/*.aux
clean-tex: clean-documents clean-education clean-experience clean-skills clean-summary ## Clean all Tex files
clean-documents: ## Clean all documents
	@rm -f documents/*.tex
clean-education: ## Clean all education
	@rm -f education/*.tex
clean-experience: ## Clean all experiences
	@rm -f experience/*.tex
clean-skills: ## Clean all skills
	@rm -f skills/*.tex
clean-summary: ## Clean all summaries
	@rm -f summary/*.tex

#:## Default Targets
.PHONY: all help

# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

help: ## This help
	@awk 'BEGIN { \
		print "LaTeX Makefile";\
	\
		FS = ":.*?## "} \
	/^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2} \
	/^#:## / {printf "\n\033[35m%s\033[0m\n", $$2} ' \
	$(MAKEFILE_LIST)

all: $(DOCUMENTS) ## Default target to generate all PDFs


.DEFAULT_GOAL := help
