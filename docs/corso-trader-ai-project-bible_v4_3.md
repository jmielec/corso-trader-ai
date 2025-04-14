**Project Bible v4.3: High R:R Trading Decision Support System (FINAL - Post OSS Review)**

**Document Version:** 4.3 (Final Pre-Development Version, incorporating OSS review)
**Date:** April 14, 2025 (Simulated Date)
**Author:** AI Assistant (Claude 3 Opus, incorporating feedback synthesis) & User
**Status:** Planning - FINAL - Ready for Phased Development

**Table of Contents:**

1.  **Vision & Mission**
2.  **Guiding Principles (Refined)**
3.  **High-Level Needs & Limitations**
4.  **Development Philosophy & Process (Refined - includes Cost Opt & OSS Strategy)**
5.  **System Architecture: Vertical Multi-Context Pipeline**
    5.1. Layers Overview
    5.2. The Context Dictionary (`context_dict`) (Critical - Requires Documentation)
    5.3. Orchestration (n8n)
    5.4. Note on Model Context Protocols (MCPs)
6.  **Technology Stack**
7.  **Core Components & Implementation Details (Refined - Notes on OSS)**
    7.1. Layer 0: Data Acquisition & Health
    7.2. Layer 1: Market & Instrument Context
    7.3. Layer 2: Context Filters
    7.4. Layer 3: Analysis Modules (Signal Agents) (Refined - Bespoke Logic Focus)
    7.5. Layer 4: Confluence Engine (Refined)
    7.6. Layer 5: Risk Management & Execution Logic (Refined - Bespoke Logic Focus)
    7.7. Layer 6: Execution Interface (Future Phase)
8.  **Data Management (Supabase)**
    8.1. Configuration Tables
    8.2. Logging Tables (Path-Aware)
    8.3. Core Data Tables
9.  **Error Handling & Logging Strategy (Refined)**
10. **Phased Rollout Plan (with Success Criteria - includes OSS Eval points)**
11. **Development Workflow & AI Collaboration Strategy (Refined)**
12. **Non-Negotiables & Core Tenets (Refined)**
13. **Risks & Mitigation Strategies (Refined - includes OSS, Cost)**

---

**1. Vision & Mission**

*   **(Vision):** To develop a robust, semi-automated decision-support system that identifies and manages high Risk:Reward (R:R) trading opportunities in the crypto market, empowering the user (an inexperienced developer) to execute trades with discipline and confidence while facilitating learning.
*   **(Mission):** Build a modular, explainable, and adaptable system using modern, developer-friendly tools (Python, n8n, Supabase, AI assistants), prioritizing risk management, context-awareness, and continuous improvement through data analysis and iterative development. The system should support a specific trading style: capturing significant gains from A+++++ setups while aggressively cutting losses, managing risk dynamically through strategies like reentries and scaling, and leveraging hyper-contextualization.

**2. Guiding Principles (Refined)**

1.  **Risk Management is Supreme:** No opportunity justifies violating predefined risk limits (per trade idea, daily, weekly). Dynamic risk adaptation is key, but always within overarching constraints. *No major losses.*
2.  **Explainability & Transparency:** Every decision, state change, signal, and configuration must be logged with rationale. *If you can't explain it, you can't trust it.* (Path-Aware Logging).
3.  **Hyper-Contextualization is Key:** Decisions must be rooted in a deep understanding of the current environment, encompassing market state, instrument characteristics, macro bias, time-based patterns, and risk posture. *Context First, Analysis Second.*
4.  **Modularity & Maintainability:** Independent, testable components. Easy to add, remove, or modify logic. Core orchestration via n8n, configuration via Supabase.
5.  **Data Robustness & Health:** Prioritize reliable data sources. Implement checks for data integrity and timeliness. Garbage in, garbage out.
6.  **AI-Assisted Development & Learning:** Leverage AI (Cursor, ChatGPT/Claude/Gemini) extensively for coding, debugging, testing, analysis, and learning, but *verify* AI output. The user must strive to *understand* the code.
7.  **Phased & Iterative Development:** Build complexity gradually. Focus on delivering value in manageable chunks (MVP per phase). Learn and adapt. Define clear success criteria for each phase.
8.  **Data-Driven Adaptation & Improvement:** The system must learn from its performance. Use path-aware logs and performance metrics (via Rating System) to refine strategies and parameters empirically.
9.  **Pragmatism & Robustness:** Favor practical, understandable solutions tailored to user limitations over "enterprise best practices" where justified. Employ developer-friendly patterns (templates, visual tools) but integrate simple, high-value robustness measures like **explicit type hinting and input validation**.

**3. High-Level Needs & Limitations**

*   **User:** Solo, inexperienced developer.
*   **Reliance:** Heavy dependence on AI (Cursor, LLMs), Supabase, n8n.
*   **Learning:** Strong desire to learn development and trading concepts through building.
*   **Goal:** Create a *profitable* decision-support system, not fully automated trading initially.
*   **Trading Style:** High R:R, aggressive loss cutting, dynamic invalidation, reentry on confirmation, scaling in/out, Pareto principle (A+++++ setups), context-driven.
*   **Constraint:** Complexity must be managed carefully to avoid overwhelm and ensure maintainability. Small account size requires focus on cost efficiency.

**4. Development Philosophy & Process (Refined - includes Cost Opt & OSS Strategy)**

*   **Lean & Pragmatic:** Focus on delivering functional increments quickly.
*   **Test As You Build:** Use mini-sandboxes (scripts, n8n test flows, notebooks) for each module. Validate I/O and rationale *before* integration. Perform **Unit Testing** on Python modules.
*   **AI Copilot Usage (High Frequency):** Ask AI for help *immediately*. Maintain a **Library of Effective Prompt Templates**. Use testing to verify AI code.
*   **Template-Driven Development:** Use standardized function/module templates (Python, n8n nodes) including **Type Hints**.
*   **Configuration as Switchboard:** Maximize use of Supabase for parameters, feature flags, routing logic.
*   **Copy-Paste-Refactor:** Clone similar modules, tweak, then refactor with AI assist.
*   **Mini-Projects per Phase:** Treat each phase's deliverable as a small project with clear **Success Criteria** and isolated tests.
*   **Visual Orchestration First:** Prefer n8n for high-level workflows, branching, scheduling; Python for complex computation/analysis/stateful logic.
*   **Structured Logging:** Consistent, machine-readable (JSON) logs with context paths.
*   **Regular AI Reviews:** At phase milestones, review structure, complexity, code quality.
*   **Simple Robustness:** Integrate **explicit Type Hinting** and **Input Validation Checks**.
*   **Focus on Tool Mastery Incrementally:** Learn tools stepwise following the phased plan.
*   **Cost Optimization (NEW):** Actively manage development and operational costs:
    *   Optimize AI prompts for efficiency (conciseness, clarity).
    *   Cache results where possible (e.g., static data, non-real-time calculations).
    *   Monitor cloud service usage (Supabase, n8n) via dashboards to stay within free/low-cost tiers.
    *   Set usage alerts for Supabase (e.g., database size, function invocations) if available.
    *   Have a contingency plan if free tiers are exceeded (e.g., prioritizing features, potential migration to self-hosting or local storage for non-critical logs).
    *   Prioritize free, permissively licensed open-source tools over paid alternatives.
*   **Open-Source Strategy (NEW/REFINED):** Leverage OSS selectively to accelerate development for standard tasks, while maintaining control and simplicity for core logic:
    *   **Prioritize:** Well-maintained libraries for **commodity tasks**:
        *   Exchange API: `CCXT`
        *   Technical Indicators: `pandas-ta` or `TA-Lib` wrapper
        *   Database Client: `supabase-py`
        *   RSS Feeds: `feedparser`
        *   Data Handling: `Pandas`, `NumPy`
    *   **Consider (with Caution):** Components from broader frameworks if genuinely simpler for specific tasks:
        *   Data Handling (L0): Lightweight data fetching/validation components from `freqtrade` *could* be explored if simpler than bespoke CCXT calls, but verify complexity.
        *   Backtesting Infrastructure (Phase 6): Evaluate frameworks like `freqtrade` or `backtrader` vs. building a simpler custom backtesting loop that directly uses your pipeline components. Choose the path with less integration friction and better validation of *your* core logic.
    *   **Avoid (Initially):** Complex frameworks for core logic:
        *   Agent Frameworks (`LangChain`, `ACE_Framework`, etc.): **Do not use for Layer 3-5 core logic.** Build bespoke Python functions for signal agents, confluence, and risk/scaling logic. This maintains transparency, control, simplifies debugging, and aligns better with learning goals.
        *   NLP/Sentiment (Phase 7+): When needed, use focused libraries like Hugging Face `transformers` directly rather than embedding within larger frameworks prematurely.
    *   **Process:** Introduce OSS one library at a time. Sandbox test thoroughly. Check license (prefer MIT/Apache) and maintenance activity. Use AI to assist integration, but *you* own the decision and validation.

**5. System Architecture: Vertical Multi-Context Pipeline**

**(Conceptual Flow):** Data -> Context Layers -> Filtering -> Analysis -> Confluence -> Risk/Execution Logic -> Decision Support Output

**5.1. Layers Overview**

*   **Layer 0: Data Acquisition & Health:** Fetches market data (price, volume), potentially news feeds, on-chain data (future). Performs basic health checks (staleness, gaps, outliers). (Managed by n8n workflows, Python scripts).
*   **Layer 1: Market & Instrument Context:** Enriches raw data with derived context about the environment. *No trading logic here.* (Python Modules triggered by n8n). Modules: `Market_State`, `Session_Timing`, `Instrument_Intelligence`, `Dynamic_Market_Bias`, `Key_Level`.
*   **Layer 2: Context Filters:** Gates based on context. *Simple boolean logic.* (n8n Switch nodes or Python functions). Filters: Time, Volatility, Risk State, Instrument Type, Market Bias.
*   **Layer 3: Analysis Modules (Signal Agents):** Performs specific TA. Generates potential signals with rationale. (Bespoke Python modules). Examples: `ICT_Agent`, `SMC_Agent`, `Pattern_Agent`, `Reentry_Signal_Agent`.
*   **Layer 4: Confluence Engine:** Aggregates signals, scores/weights them (initially simple, later using ratings), identifies A+++++ setups. (Bespoke Python module).
*   **Layer 5: Risk Management & Execution Logic:** Applies risk rules, determines size, manages trade lifecycle (stops, scaling, reentries), monitors invalidation. (Bespoke Python module(s)). Includes: `Position_Sizing`, `Trade_Invalidation`, `Scaling_Engine`, `Trade_Idea_Manager`.
*   **Layer 6: Execution Interface:** (Future Phase) Translates commands to exchange API calls.

**5.2. The Context Dictionary (`context_dict`) (Critical - Requires Documentation)**

*   Central Python dictionary passed through the pipeline, progressively enriched.
*   **Requires meticulous external documentation** (e.g., Markdown file in Git repo) detailing each key, type, source, purpose.
*   Key Fields (Examples): `instrument_symbol`, `instrument_category`, `market_bias`, `day_of_week`, `market_state`, `key_levels`, `active_trade_idea_id`, risk/position state, etc.

**5.3. Orchestration (n8n)**

*   Manages workflow, schedules tasks, triggers Python scripts (Execute Command/HTTP), handles conditional routing (Switch).

**5.4. Note on Model Context Protocols (MCPs)**

*   Stick to explicit `context_dict` passing for simplicity and transparency.

**6. Technology Stack**

*   **Orchestration:** n8n (Self-hosted or Cloud)
*   **Backend Logic:** Python 3.10+
*   **Database & Config:** Supabase (PostgreSQL, JSONB)
*   **Data Science Libraries:** Pandas, NumPy, TA-Lib wrapper / pandas-ta
*   **Exchange Interaction:** CCXT
*   **Development Environment:** VS Code + Cursor extension
*   **AI Assistance:** Cursor, Direct LLM APIs/Interfaces
*   **Version Control:** Git
*   **(Potential RSS):** feedparser
*   **(Potential DB Client):** supabase-py

**7. Core Components & Implementation Details (Refined - Notes on OSS)**

7.1. **Layer 0: Data Acquisition & Health**
    *   Use `CCXT` for price/volume. Consider simple `freqtrade` components *only if* clearly beneficial over direct CCXT usage. Use `feedparser` for RSS. Implement health checks.
7.2. **Layer 1: Market & Instrument Context**
    *   Use `pandas-ta` or `TA-Lib` wrapper for indicators within modules.
7.3. **Layer 2: Context Filters** *(Unchanged)*
7.4. **Layer 3: Analysis Modules (Signal Agents) (Refined - Bespoke Logic Focus)**
    *   **Build bespoke Python functions** following standard template (with Type Hints, Input Validation). Use `pandas-ta`/`TA-Lib`. **Do not integrate complex external agent frameworks (LangChain, ACE).** Focus on clear, testable implementations of ICT, SMC, pattern logic etc. Return standard signal dict.
7.5. **Layer 4: Confluence Engine (Refined)**
    *   **Build bespoke Python logic.** Start simple (signal counting/averaging), enhance with `Performance_Ratings` weighting later (Phase 7+).
7.6. **Layer 5: Risk Management & Execution Logic (Refined - Bespoke Logic Focus)**
    *   **Build bespoke Python logic** for Position Sizing, Invalidation, Scaling Engine, Trade Idea Manager. Requires careful implementation and testing. Robust validation is critical.
7.7. **Layer 6: Execution Interface (Future Phase)**
    *   Use `CCXT`.

**8. Data Management (Supabase)**
    * 8.1. **Configuration Tables:** `System_Config`, `Asset_Config`, `Filter_Config`, `Agent_Config`, `Risk_Config` (use JSONB for flexible rules).
    * 8.2. **Logging Tables (Path-Aware):** `Pipeline_Log` (JSONB context snapshot), `Error_Log`.
    * 8.3. **Core Data Tables:** `Instruments`, `Instrument_News`, `Key_Levels`, `Trade_Ideas`, `Trades`, `Performance_Ratings` (*later phases*). (Schema details from v4.2 remain valid).

**9. Error Handling & Logging Strategy (Refined)**
    *   Use `try...except`. Implement **input validation**. Log errors to `Error_Log` with context. Use structured **JSON logging** for `Pipeline_Log`. Basic alerting for critical failures. Verb-driven log messages.

**10. Phased Rollout Plan (with Success Criteria - includes OSS Eval points)**

*   **Phase 0: Setup & Foundations (1-2 weeks)**
    *   *Tasks:* Setup tools (inc. Git), basic n8n workflow (using `CCXT`), basic Python module template, Supabase schemas, logging. Evaluate simplest data fetching (direct `CCXT` vs `freqtrade` components).
    *   **Success Criteria:** Data fetching working, basic module runs, logs to Supabase, Git repo active. OSS data choice documented. **External `context_dict` documentation started.**
*   **Phase 1: Basic Context (2-3 weeks)**
    *   *Tasks:* Build Context modules (L1) using `pandas-ta`/`TA-Lib`. Manually populate `Instruments`. Enrich `context_dict`. Update `context_dict` docs.
    *   **Success Criteria:** `context_dict` logged contains accurate context data. `Instruments` table usable. Docs updated.
*   **Phase 2: Basic Filters & Signals (2-3 weeks)**
    *   *Tasks:* Implement Filters (L2). Build 1-2 simple Signal Agents (L3 - **bespoke Python functions**). Basic Confluence (L4 - simple aggregation). Update `context_dict` docs.
    *   **Success Criteria:** Pipeline routes correctly. Simple signals generated and logged. Docs updated.
*   **Phase 3: Basic Risk & Trade Ideas (3-4 weeks)**
    *   *Tasks:* Implement Market Bias (L1), relevant filters (L2). Build Position Sizing (L5 - bespoke). Basic `Trade_Ideas`/`Trades` logging (simulated). Update `context_dict` docs.
    *   **Success Criteria:** Sized trade ideas proposed & logged. Docs updated.
*   **Phase 4: Reentry Logic & Enhanced Signals (3-4 weeks)**
    *   *Tasks:* Build `Reentry_Signal_Agent` (L3 - bespoke). Enhance `Trade_Idea_Manager` (L5 - bespoke) with reentry logic. Build more L3 agents (bespoke). Refine Confluence (L4 - bespoke). Update `context_dict` docs.
    *   **Success Criteria:** Reentry logic simulated correctly per budget/rules. Docs updated.
*   **Phase 5: Basic Scaling & Invalidation (4-5 weeks) - COMPLEXITY JUMP**
    *   *Tasks:* Implement *Simple* Scaling Out, SL to BE rules (L5 - bespoke `Scaling_Engine`). Basic Trade Invalidation (L5 - bespoke). Refine schemas. Establish `Performance_Ratings` schema. Update `context_dict` docs.
    *   **Success Criteria:** Simple scaling/invalidation simulated correctly. Docs updated.
*   **Phase 6: Backtesting & Parameter Tuning (4-6 weeks)**
    *   *Tasks:* **Evaluate & Implement Backtesting:** Choose between building a custom loop vs. integrating `freqtrade`/`backtrader` infrastructure. Run tests. Populate `Performance_Ratings`.
    *   **Success Criteria:** Reliable backtesting completed. Initial ratings generated. Parameters tuned. Backtesting approach documented.
*   **Phase 7+: Advanced Features & Live Simulation (Ongoing)**
    *   *Tasks:* Dynamic signal weighting (L4). Full *Dynamic Scaling In/Out* (L5 - bespoke). News Feed automation (`feedparser`). Performance Analysis module. Integrate `transformers` for sentiment if desired. Layer 6 interface (`CCXT`) for paper trading.
    *   **Success Criteria:** Advanced features working in simulation. Paper trading operational.

**11. Development Workflow & AI Collaboration Strategy (Refined)**
    *   Use Git frequently. Follow Phased Plan & Success Criteria. Maintain **Prompt Library**. Maintain `context_dict` documentation rigorously. Use Mini-Projects/Testing. Prioritize clear AI communication.

**12. Non-Negotiables & Core Tenets (Refined)**
    *   Risk limits unbreakable. Path-aware logging. Documented `context_dict`. Modularity. Config in Supabase. Understand AI code. Adhere to Plan. Use **UTC**. Test thoroughly. **Type Hints**. **Input Validation**.

**13. Risks & Mitigation Strategies (Refined - includes OSS, Cost)**

1.  **Complexity Overwhelm (HIGH):** *Mitigation:* Phased rollout, Mini-Projects, AI assist, start simple, Success Criteria, **stick to bespoke core logic, avoid complex frameworks early.**
2.  **Implementation Errors (HIGH):** *Mitigation:* Testing (Unit, Integration, Backtesting), AI reviews, templates, logging, validation, type hints, cautious rollout.
3.  **Data Quality/API Issues (MEDIUM):** *Mitigation:* Health checks, reputable sources (CCXT), fallbacks.
4.  **Overfitting (MEDIUM):** *Mitigation:* Out-of-sample tests, regime testing, robust signals, ongoing evaluation.
5.  **AI Over-Reliance (MEDIUM):** *Mitigation:* Actively understand code, focused learning, documentation.
6.  **Cost Overruns (MEDIUM):** *Mitigation:* **Implement Cost Optimization practices** (prompt efficiency, caching, monitor usage, alerts, free tiers, local fallbacks).
7.  **Scope Creep (HIGH):** *Mitigation:* Stick to Phased Plan & Success Criteria. Use backlog for future ideas.
8.  **Motivation/Burnout (MEDIUM):** *Mitigation:* Sprints, milestones, journal, breaks, focus on learning.
9.  **OSS Integration Risks (MEDIUM):** *Mitigation:* **Selective adoption** (commodity tasks only), avoid core logic frameworks, sandbox testing, check license/activity, use AI for integration help.

---
**(End of Project Bible v4.3)**

---

**Preparing for Development: Tool Orchestration & Usage Strategy**

Now that Bible v4.3 is finalized, let's outline how we'll use the tools efficiently:

1.  **Core Runtime Orchestration:**
    *   **n8n:** Will act as the main scheduler and high-level workflow engine. It will trigger data fetching (Layer 0), potentially call Python scripts for context generation (Layer 1), apply simple filters (Layer 2), trigger analysis (Layer 3), and so on. We'll use its visual interface for defining the main pipeline flow and conditional logic (Switch nodes). Python scripts will likely be called via the `Execute Command` node or potentially simple HTTP endpoints if needed later.
    *   **Python:** Will house the computationally intensive or complex stateful logic. This includes all custom analysis agents (Layer 3), the Confluence Engine (Layer 4), and the sophisticated Risk Management/Scaling/Trade Idea logic (Layer 5). Python scripts will receive data (potentially file paths or JSON via stdin/args from n8n), perform their tasks using libraries like Pandas, TA-Lib/pandas-ta, CCXT, supabase-py, and output results (e.g., JSON to stdout) for n8n to pick up or directly interact with Supabase.
    *   **Supabase:** The central hub for configuration (read by Python/n8n), data storage (instruments, levels, etc., read by Python), and logging (written to by Python/n8n). Python scripts will use `supabase-py` to interact with it. n8n might use its built-in Postgres node or trigger Python scripts for DB interactions.

2.  **Development Environment & AI Assistance:**
    *   **VS Code + Cursor:** This is your primary *coding environment*. You'll write, edit, and debug Python code here.
    *   **Cursor's Role:** Use Cursor *constantly* within VS Code for:
        *   **Code Generation:** Generating boilerplate, function templates (following our standard), implementing specific indicator calculations, writing database queries (for `supabase-py`).
        *   **Explanation:** Understanding code snippets (both generated and existing).
        *   **Debugging:** Suggesting fixes for errors, helping interpret tracebacks.
        *   **Refactoring:** Cleaning up code, improving structure.
        *   **Test Generation:** Creating basic unit tests for Python functions/modules.
        *   **Documentation:** Assisting with writing comments and updating the external `context_dict` documentation.
    *   **Choosing LLMs within Cursor (e.g., Grok, Claude 3.x, GPT-4.x, Deepseek):**
        *   **No Single "Best":** The optimal model often depends on the specific task (e.g., one might be better at boilerplate, another at debugging complex logic). Performance also changes rapidly as models evolve.
        *   **Recommendation:** Start with a strong, general-purpose model known for coding available in Cursor (e.g., **GPT-4o or Claude 3 Opus/Sonnet** are typically excellent choices).
        *   **Experiment:** As you work through Phase 0 and 1, try different available models for various tasks. See which one provides the most accurate, helpful, and efficient responses *for you* and *this project*. Does one generate better Python? Is another better at explaining n8n concepts?
        *   **Flexibility:** Don't feel locked into one model. Use the "best tool for the job" available within Cursor at that moment. Maintain your Prompt Library to work effectively across models.
        *   **Defer Deep Optimization:** We can refine the *precise* model choice for specific micro-tasks as we gain practical experience during development. The key now is to leverage *AI assistance effectively*, regardless of the specific underlying model.

3.  **Version Control:**
    *   **Git:** Use Git diligently from the very beginning (Phase 0). Commit frequently with clear messages after completing logical units of work (e.g., "Implemented Market State module," "Added Instrument schema to Supabase"). This provides a safety net and history.

**Next Step: Commence Phase 0**

We are now ready to start development according to the **Phased Rollout Plan (Section 10)** in Bible v4.3. The first objectives for **Phase 0 (Setup & Foundations)** are:

1.  Set up your development environment (Python, VS Code + Cursor, n8n instance, Supabase account).
2.  Initialize a Git repository for the project.
3.  Build a basic n8n workflow using `CCXT` (triggered manually or on a simple schedule) to fetch price data for one or two test symbols (e.g., BTCUSDT).
4.  Define the initial Supabase schemas (start with `Pipeline_Log`, basic `Instruments`, basic `Configuration`).
5.  Create a basic Python module template (e.g., a simple function that takes a symbol, perhaps fetches data path/config from args/env, prints "Hello", includes Type Hints).
6.  Connect n8n to execute this basic Python script.
7.  Implement basic logging from both n8n and the Python script to the `Pipeline_Log` table in Supabase (initially just logging timestamps and simple messages).
8.  Evaluate and decide on the initial data fetching approach (direct `CCXT` vs. exploring `freqtrade` components) and document the choice.
9.  Start the external `context_dict` documentation file (e.g., `context_dict_schema.md`) in your Git repo, defining the very first basic fields (like `timestamp`, `symbol`).

Let me know when you're ready to tackle the first task of Phase 0!