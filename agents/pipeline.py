"""Orchestrate the four specialist agents."""

from .base import create_client
from .brand_analysis_agent import BrandAnalysisAgent
from .logo_concept_agent import LogoConceptAgent
from .prompt_optimizer_agent import PromptOptimizerAgent
from .design_review_agent import DesignReviewAgent


class LogoDesignPipeline:
    def __init__(self, model: str = "gemini-2.5-flash"):
        self.client = create_client()
        self.model = model
        self.brand_agent = BrandAnalysisAgent()
        self.concept_agent = LogoConceptAgent()
        self.optimizer_agent = PromptOptimizerAgent()
        self.review_agent = DesignReviewAgent()

    def run(self, brief: str) -> dict[str, str]:
        if not brief.strip():
            raise ValueError("The client brief is empty.")
        strategy = self.brand_agent.run(self.client, brief, self.model)
        concepts = self.concept_agent.run(self.client, brief, strategy, self.model)
        prompt_package = self.optimizer_agent.run(self.client, brief, strategy, concepts, self.model)
        review = self.review_agent.run(self.client, brief, prompt_package, self.model)
        return {"brand_analysis": strategy, "logo_concepts": concepts, "optimized_prompt": prompt_package, "design_review": review}
