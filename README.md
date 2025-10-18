# research_agent
The research agent is an agentic researcher who is implemented using a reflection workflow. 
Based on the user research topic, the LLM will draft an initial version of the research paper, which will then be passed to another LLM (possibly the same one) for reflection by indicating what the LLM needs to reflect.
The second LLM will reflect on its work and provide feedback, which is then passed back either to the same LLM or to another LLM to write the final version.
