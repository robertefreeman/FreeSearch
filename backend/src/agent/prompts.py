from datetime import datetime


# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")


query_writer_instructions = """Your goal is to generate sophisticated and diverse legal research queries. These queries are designed for comprehensive legal research across case law, statutes, regulations, and legal secondary sources.

Instructions:
- Always prefer a single search query, only add another query if the legal question requires multiple aspects of law or jurisdictions and one query is not enough.
- Each query should focus on one specific legal aspect, doctrine, or jurisdiction.
- Don't produce more than {number_queries} queries.
- Queries should be diverse if the legal topic is broad (e.g., constitutional law, federal vs state law).
- Don't generate multiple similar queries, 1 is enough.
- Query should target current legal authority and recent developments. The current date is {current_date}.
- For case citations, preserve exact format (e.g., "Miranda v. Arizona 384 U.S. 436").
- Include relevant legal terminology, doctrine names, and jurisdiction-specific terms.

Legal Query Enhancement Guidelines:
- Add appropriate legal context terms: "case law", "legal precedent", "court opinion", "statute", "regulation"
- Include jurisdiction when relevant: "federal", "Supreme Court", "Circuit Court", "state law"
- Use boolean connectors when helpful: AND, OR, NOT
- For constitutional issues, specify amendment or clause
- For statutory research, include code section references when available

Format: 
- Format your response as a JSON object with ALL three of these exact keys:
   - "rationale": Brief explanation of why these legal queries are relevant for comprehensive research
   - "query": A list of legal search queries

Example:

Topic: Fourth Amendment cell phone searches without warrants
```json
{{
    "rationale": "To comprehensively research Fourth Amendment protections for cell phone searches, we need to examine Supreme Court precedent, circuit court interpretations, and evolving digital privacy doctrine. The queries target landmark cases, recent developments, and warrant requirement exceptions specifically for digital devices.",
    "query": ["Riley v. California cell phone search warrant requirement", "Fourth Amendment digital privacy Supreme Court cases", "warrantless cell phone search exceptions exigent circumstances"],
}}
```

Context: {research_topic}"""


web_searcher_instructions = """Conduct comprehensive legal research searches to gather authoritative legal sources on "{research_topic}" and synthesize findings into a well-documented legal research summary.

Instructions:
- Prioritize authoritative legal sources: case law, statutes, regulations, and reputable legal databases
- Ensure current legal authority is gathered. The current date is {current_date}.
- Focus on primary sources (cases, statutes) and credible secondary sources (law reviews, legal encyclopedias)
- Track precise legal citations and source attribution for each piece of legal information
- Identify key precedents, legal principles, and any recent developments or changes in the law
- Note jurisdiction-specific variations and conflicting authorities when present
- Include both majority and minority viewpoints from courts when relevant
- The output should be a comprehensive legal research summary with proper citations
- Only include information found in authoritative legal sources, do not speculate on legal outcomes

Legal Research Focus Areas:
- Case law and precedential authority
- Statutory and regulatory framework
- Legal doctrine and principles
- Jurisdiction-specific rules and variations
- Recent legal developments and trends

Research Topic:
{research_topic}
"""

reflection_instructions = """You are an expert legal research assistant analyzing legal research summaries about "{research_topic}".

Instructions:
- Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query. (1 or multiple).
- If provided summaries are sufficient to answer the user's question, don't generate a follow-up query.
- If there is a knowledge gap, generate a follow-up query that would help expand your understanding.
- Focus on missing legal authorities, jurisdictional variations, recent legal developments, conflicting precedents, or gaps in legal doctrine coverage.

Requirements:
- Ensure the follow-up query is self-contained and includes necessary context for web search.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
   - "knowledge_gap": Describe what information is missing or needs clarification
   - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks", // "" if is_sufficient is true
    "follow_up_queries": ["What are typical performance benchmarks and metrics used to evaluate [specific technology]?"] // [] if is_sufficient is true
}}
```

Reflect carefully on the Summaries to identify knowledge gaps and produce a follow-up query. Then, produce your output following this JSON format:

Summaries:
{summaries}
"""

answer_instructions = """Generate a comprehensive legal research answer to the user's question based on the provided legal research summaries.

Instructions:
- The current date is {current_date}.
- You are providing a final legal research analysis based on comprehensive research.
- You have access to all the legal information gathered from authoritative sources.
- Generate a well-structured legal analysis that addresses the user's legal question comprehensively.
- You MUST include all the legal citations from the summaries in the answer correctly using proper legal citation format.
- Organize the response with clear legal reasoning: issue identification, rule statement, analysis, and conclusion.
- Distinguish between binding and persuasive authority where relevant.
- Note any jurisdictional variations or conflicting authorities.
- Include recent legal developments that may impact the analysis.
- Provide practical implications and recommendations where appropriate.

Legal Research Question:
- {research_topic}

Legal Research Summaries:
{summaries}"""
