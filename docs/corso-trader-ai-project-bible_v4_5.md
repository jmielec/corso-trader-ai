**Project Bible v4.5: High R:R Trading Decision Support System**

**Document Version:** 4.5 (Final Pre-Development Version - Incorporating Dynamic Risk & Advanced Modularity)
**Date:** April 14, 2025 (Simulated Date)
**Author:** AI Assistant (Claude 3 Opus, incorporating feedback synthesis) & User
**Status:** Planning - FINAL - Ready for Phased Development

**Table of Contents:**

1.  **Vision & Mission**
2.  **Guiding Principles (Refined & Expanded - includes Radical Modularity)**
3.  **High-Level Needs & Limitations**
4.  **Development Philosophy & Process (Refined - Emphasizes Registry & Infrastructure)**
5.  **System Architecture: Vertical Multi-Context Pipeline (Registry-Driven)**
    5.1. Layers as Execution Slots
    5.2. The Context Dictionary (`context_dict`) (Contract Enforcement)
    5.3. Orchestration (Registry-Aware Python Orchestrator + n8n)
    5.4. Note on Model Context Protocols (MCPs)
    5.5. Strategy Note: Dynamic, Modular Context-Aware Risk Allocation
    5.6. Strategy Note: Registry-Driven Pipeline Assembly
    5.7. Summary Table: Context & Risk Module Interaction Concept
6.  **Technology Stack**
7.  **Core Components & Implementation Details (Module-Oriented)**
    7.1. Layer 0: Data Acquisition & Health
    7.2. Layer 1 Modules: Market & Instrument Context
    7.3. Layer 2 Modules: Context Filters
    7.4. Layer 3 Modules: Analysis Modules (Signal Agents)
    7.5. Layer 4 Modules: Confluence Engine
    7.6. Layer 5 Modules: Risk Management & Execution Logic
    7.7. Layer 6: Execution Interface (Future Phase)
    7.8. Code Directory Structure
8.  **Data Management (Supabase - includes Module Registry)**
    8.1. `Module_Registry` Table (NEW & CRITICAL)
    8.2. Configuration Tables (Referencing `module_id`)
    8.3. Logging Tables (Including `module_id`/`version`)
    8.4. Core Data Tables
9.  **Error Handling & Logging Strategy (Module-Aware)**
10. **Phased Rollout Plan (Revised - Infrastructure First)**
11. **Development Workflow & AI Collaboration Strategy (Registry Focus)**
12. **Non-Negotiables & Core Tenets (Registry Integrity)**
13. **Risks & Mitigation Strategies (Includes Infrastructure Complexity)**

---

**1. Vision & Mission**

*   **(Vision):** To develop a robust, semi-automated decision-support system that identifies and manages high Risk:Reward (R:R) trading opportunities in the crypto market, empowering the user (an inexperienced developer) to execute trades with discipline and confidence while facilitating learning.
*   **(Mission):** Build a modular, explainable, and adaptable system using modern, developer-friendly tools (Python, n8n, Supabase, AI assistants), prioritizing risk management, context-awareness, and continuous improvement through data analysis and iterative development. The system should support a specific trading style: capturing significant gains from A+++++ setups while aggressively cutting losses, managing risk dynamically through strategies like reentries and scaling, and leveraging hyper-contextualization, **including macro market conditions**.

**2. Guiding Principles (Refined & Expanded - includes Radical Modularity)**

1.  **Risk Management is Supreme:** No opportunity justifies violating predefined risk limits. Dynamic risk adaptation is key, but always within overarching constraints. *No major losses.*
2.  **Explainability & Transparency:** Every decision, state change, signal, and configuration must be logged with rationale, tagged by the specific module and version responsible. *If you can't trace it, you can't trust it.* (Path-Aware, Module-Tagged Logging).
3.  **Hyper-Contextualization is Key:** Decisions must be rooted in a deep understanding of the current environment, encompassing market state, instrument characteristics, macro bias, time-based patterns, **broad market indicators (e.g., Dominance, Capital Flows)**, and risk posture, all processed via explicit context modules. *Context First, Analysis Second.*
4.  **Radical Modularity:** All logic—context building, signal generation, filtering, confluence, risk/execution—is comprised of discrete, **registry-tracked modules**. The pipeline is assembled dynamically by configuration, not by hardcoded sequencing.
5.  **Strict Interface Contracts:** Every module's interaction with the central `context_dict` is explicitly documented (`context_dict_schema.md`, Module Registry, docstrings) and externally maintained. Modules must adhere strictly to these contracts. **No module may depend on undocumented external state.**
6.  **Registry-Driven Routing:** Orchestration dynamically selects and executes modules based on the `Module_Registry` and associated configuration, not hardcoded names or paths.
7.  **Plug-and-Play Evolution:** Modules can be safely added, removed, versioned, branched, or run in parallel (A/B testing) at any pipeline stage, solely through registry/config updates, minimizing orchestration code changes.
8.  **Data Robustness & Health:** Prioritize reliable data sources. Implement checks for data integrity and timeliness. Garbage in, garbage out.
9.  **AI-Assisted Development & Learning:** Leverage AI extensively for coding, debugging, testing, analysis, and learning, but *verify* AI output. The user must strive to *understand* the code.
10. **Phased & Iterative Development:** Build complexity gradually. Focus on delivering value in manageable chunks, prioritizing robust infrastructure first. Learn and adapt. Define clear success criteria for each phase.
11. **Data-Driven Adaptation & Improvement:** The system must learn from its performance. Use path-aware, module-tagged logs and performance metrics (via Rating System) to refine strategies and parameters empirically via registry and configuration updates.
12. **Pragmatism & Robustness:** Favor practical, understandable solutions tailored to user limitations over "enterprise best practices" where justified. Employ developer-friendly patterns but integrate simple, high-value robustness measures like **explicit Type Hinting** and **Input Validation**. **Acknowledge that the registry adds upfront complexity for significant long-term robustness and flexibility.**
13. **Market Context-Driven Risk:** Risk allocation and trade aggressiveness are dynamic, governed by real-time analysis of macro crypto market indicators (e.g., USDT.D, BTC.D, OTHERS.D, TOTAL), interpreted through specific, registered **context analyzer modules**, not hardcoded heuristics or static rules.
14. **Separable, Modular Signal and Risk Blocks:** Every context detector (including market-wide indicators), signal generator, filter rule, and risk budgeting logic is implemented as a swappable, **registry-tracked module**, with fully documented I/O contracts and rationale.

**3. High-Level Needs & Limitations**

*   **User:** Solo, inexperienced developer.
*   **Reliance:** Heavy dependence on AI (Cursor, LLMs), Supabase, n8n.
*   **Learning:** Strong desire to learn development and trading concepts through building.
*   **Goal:** Create a *profitable* decision-support system, not fully automated trading initially.
*   **Trading Style:** High R:R, aggressive loss cutting, dynamic invalidation, reentry on confirmation, scaling in/out, Pareto principle (A+++++ setups), context-driven (including market regime).
*   **Constraint:** Complexity must be managed carefully to avoid overwhelm and ensure maintainability. Small account size requires focus on cost efficiency. **The advanced modularity adds upfront complexity.**

**4. Development Philosophy & Process (Refined - Emphasizes Registry & Infrastructure)**

*   **Build Infrastructure First:** Prioritize setting up the `Module_Registry` schema, the `context_dict_schema.md`, and the basic dynamic Python orchestrator script in Phase 0/1. **This is crucial.**
*   **Registry as Source of Truth:** All development assumes logic components are defined, versioned, activated, and controlled via the `Module_Registry` and associated configuration tables in Supabase.
*   **Module Creation Workflow:**
    1.  Define required/produced keys and document them in `context_dict_schema.md`.
    2.  Create module code (e.g., `/modules/context/new_module_v1.py`) following standard templates (type hints, input validation, logging, clear function entry point).
    3.  Add a detailed entry to the `Module_Registry` table in Supabase (metadata, path, function, I/O keys, version, status).
    4.  Write comprehensive unit tests for the module in isolation.
    5.  Activate/configure the module's usage via relevant Config tables (e.g., `Pipeline_Config`, `Strategy_Config`) referencing its `module_id`.
*   **Template-Driven Development:** Use standardized function/module templates (Python) including Type Hints, standard logging calls, and error handling. Use templates for `Module_Registry` entries.
*   **Test As You Build:** Use mini-sandboxes/scripts for initial dev. **Perform Unit Testing** on all Python modules. Integration tests verify the registry-driven pipeline flow.
*   **Configuration as Switchboard:** Maximize use of Supabase for parameters, feature flags, module selection, risk rules, and pipeline routing logic.
*   **AI Copilot Usage (High Frequency):** Use AI for generating module code, tests, registry entries, documentation updates, debugging. Maintain **Library of Effective Prompt Templates**. *Verify AI code.*
*   **Structured Logging:** Consistent, machine-readable (JSON) logs tagged with `module_id`, `version`, context paths, and rationale strings.
*   **Regular AI Reviews:** Review structure, complexity, code quality, registry consistency at milestones.
*   **Focus on Tool Mastery Incrementally:** Learn tools stepwise following the phased plan.
*   **Cost Optimization:** Actively manage development and operational costs (prompt efficiency, caching, monitor usage, alerts, free tiers, local fallbacks).
*   **Open-Source Strategy:** Leverage OSS selectively (**Prioritize:** `CCXT`, `pandas-ta`, `TA-Lib` wrapper, `supabase-py`, `Pandas`, `NumPy`, `feedparser`. **Avoid:** Complex frameworks like `LangChain` or `ACE` for core logic Layers 1-5). Introduce libraries carefully, test thoroughly, check license, use AI for integration help but own validation.

**5. System Architecture: Vertical Multi-Context Pipeline (Registry-Driven)**

**(Conceptual Flow):** n8n Trigger -> Python Orchestrator -> Registry Lookup -> Execute Layer 1 Modules -> Registry Lookup -> Execute Layer 2 Modules -> ... -> Final `context_dict` -> Decision Support Output / Log

**5.1. Layers as Execution Slots**
    *   Pipeline layers (1-5) are conceptual stages within the Python orchestrator's logic. The actual computational logic executed within each layer is determined at runtime by querying the `Module_Registry` based on the current `context_dict` state (e.g., asset type, market regime derived by a previous module) and pipeline/strategy configuration tables. A layer might execute zero, one, or multiple registered modules, potentially in a defined sequence or concurrently if the orchestrator and modules are designed for it (initially sequential is simpler).

**5.2. The Context Dictionary (`context_dict`) (Contract Enforcement)**
    *   The central Python dictionary passed sequentially *through* the selected modules within the Python orchestrator. Modules read from and write to this dictionary.
    *   **`context_dict_schema.md`**, maintained in the Git repository, is the **canonical definition** of all allowed keys, their data types, intended meaning, and which module `logic_type` typically produces them.
    *   The `Module_Registry` entries (`input_keys`, `output_keys`) explicitly reference keys defined in this schema. **Strict adherence by all modules is mandatory for system stability.**

**5.3. Orchestration (Registry-Aware Python Orchestrator + n8n)**
    *   **n8n:** Acts as the **high-level scheduler** (e.g., time-based triggers, webhook triggers) and **initial trigger** for the main pipeline. It might perform very basic initial data gathering (e.g., list of symbols to process) and then **calls the main Python orchestrator script** (likely via `Execute Command` node), passing necessary initial parameters (e.g., trigger type, symbols). It receives the final status or key results back from the Python script for potential simple actions (e.g., basic notification).
    *   **Python Orchestrator (e.g., `pipeline_runner.py`):** This is the **core runtime engine**. It is responsible for:
        1.  Receiving initial parameters from n8n.
        2.  Initializing the `context_dict`.
        3.  Establishing connection to Supabase.
        4.  Iterating through the defined pipeline layers/stages (e.g., Context -> Filter -> Analysis -> Confluence -> Risk).
        5.  **For each stage:** Querying the `Module_Registry` and relevant Config tables (e.g., `Pipeline_Config`, `Strategy_Config`) to determine *which active module(s)* (`module_id`s) should run based on the current `context_dict` and configuration.
        6.  **Dynamically importing/loading** the Python code specified by the `script_path` in the registry for the selected modules.
        7.  **Executing** the designated function (`function_name`) within each loaded module, passing the mutable `context_dict` to it.
        8.  Handling context updates returned by or modified within the `context_dict` by modules.
        9.  Implementing robust error handling around module loading and execution.
        10. Orchestrating logging (using a shared utility) ensuring logs are tagged with `module_id`, `version`.
        11. Returning final status/results to n8n.

**5.4. Note on Model Context Protocols (MCPs)**
    *   Stick to the explicit `context_dict` passing mechanism managed by the Python orchestrator for simplicity, transparency, and adherence to defined contracts.

**5.5. Strategy Note: Dynamic, Modular Context-Aware Risk Allocation**
> The system's risk posture is dynamically adjusted based on market conditions. This is achieved via specific, registered **Market Context Analyzer modules** (Layer 1) that analyze macro indicators (USDT.D, BTC.D, etc.) and output standardized signals (e.g., `market_regime`, `usdt_d_trend`) into the `context_dict`. Subsequent filtering (Layer 2 modules) and risk calculation (Layer 5 **Dynamic Risk Allocator modules**) consume these signals. Configurable rules (in Supabase `Risk_Config`) map these signals to concrete risk parameters (e.g., risk multipliers, category caps, max positions), which are then applied by the risk modules. This ensures risk is context-aware, configurable, and traceable.

**5.6. Strategy Note: Registry-Driven Pipeline Assembly**
> The core pipeline logic is **not hardcoded**. Instead, the Python orchestrator script dynamically assembles and executes the pipeline at runtime based on definitions stored in the Supabase **`Module_Registry`** and associated configuration tables. Each functional unit (context analysis, filtering, signal generation, confluence, risk management) is an independent, versioned Python module registered with its metadata, path, entry function, and I/O contract keys. This architecture allows adding, removing, versioning, or A/B testing logic components solely through database updates, providing maximum flexibility, maintainability, and future-proofing without requiring changes to the orchestrator's core structure. Adherence to the documented `context_dict_schema.md` contract is paramount.

**5.7. Summary Table: Context & Risk Module Interaction Concept**

| Module `logic_type`     | Layer | Input from `context_dict` / Config | Output/Effect to `context_dict` / Pipeline         | Controlled by Registry/Config? | Adheres to `context_dict` schema? |
| :---------------------- | :---- | :--------------------------------- | :------------------------------------------------- | :----------------------------- | :-------------------------------- |
| `context` (Market)    | 1     | Raw Market Data, Config          | Regime/Context signals (e.g., `market_regime`)     | Yes                            | Yes                               |
| `context` (Instrument)| 1     | Raw Instrument Data, Config      | Instrument state (e.g., `volatility`, `key_levels`) | Yes                            | Yes                               |
| `filter`                | 2     | Context signals, Config Rules    | Allow/Block pipeline continuation (via log/flag) | Yes                            | Yes                               |
| `agent`                 | 3     | Context, Instrument Data, Config | Trade signals/ideas (dict/object)                | Yes                            | Yes                               |
| `confluence`            | 4     | Multiple Agent Signals, Config   | Scored/Confirmed trade ideas                     | Yes                            | Yes                               |
| `risk` (Allocator)    | 5     | Context signals, Config Rules    | Dynamic Risk params (e.g., `allowed_risk_size`)    | Yes                            | Yes                               |
| `risk` (Sizing)       | 5     | Trade Idea, Risk Params, Config  | Position size, SL/TP levels                      | Yes                            | Yes                               |
| `risk` (Management)   | 5     | Active Trade State, Context      | Invalidation flags, Scaling actions                | Yes                            | Yes                               |

**6. Technology Stack**

*   **Orchestration Trigger/Schedule:** n8n (Hosted on Render)
*   **Core Logic Execution:** Python 3.10+ (via a central orchestrator script)
*   **Database & Configuration:** Supabase (PostgreSQL, relies heavily on JSONB for config flexibility)
*   **Data Science Libraries:** Pandas, NumPy
*   **Technical Indicators:** TA-Lib wrapper / pandas-ta
*   **Exchange Interaction:** CCXT
*   **Development Environment:** VS Code + Cursor extension
*   **AI Assistance:** Cursor, Direct LLM APIs/Interfaces
*   **Version Control:** Git (GitHub)
*   **(Potential) RSS Feeds:** feedparser
*   **Database Client (Python):** supabase-py

**7. Core Components & Implementation Details (Module-Oriented)**

*   **General:** All components in Layers 1-5 are implemented as distinct Python (*.py*) files, each containing one or more functions callable by the orchestrator. Each logical unit corresponds to an entry in the `Module_Registry`.
*   7.1. **Layer 0: Data Acquisition & Health:**
    *   Tasks likely performed by initial n8n steps or dedicated Python scripts *before* the main orchestrator runs, or by specific Layer 1 modules if dynamic fetching is needed.
    *   Fetches Price/Volume (`CCXT`), Macro Indicators (e.g., `CCXT` for dominance, specific APIs, or data provider files), RSS (`feedparser`). Performs health checks. Results are fed into the initial `context_dict` or accessed by modules as needed.
*   7.2. **Layer 1 Modules: Market & Instrument Context** (`logic_type`: "context")
    *   Examples: `Market_State_Analyzer_v1.py`, `Session_Timing_v1.py`, `Instrument_Intelligence_v1.py`, `USDT_D_Analyzer_v1.py`, `BTC_D_Analyzer_v1.py`, `Key_Level_Finder_v1.py`.
    *   Consume raw data, apply indicators (`pandas-ta`), output derived state variables to `context_dict`.
*   7.3. **Layer 2 Modules: Context Filters** (`logic_type`: "filter")
    *   Examples: `Volatility_Filter_v1.py`, `Min_Volume_Filter_v1.py`, `Risk_Off_Alt_Blocker_v1.py`, `Session_Filter_v1.py`.
    *   Read context variables from `context_dict`, apply simple boolean logic based on Config rules. Typically output a boolean flag or log a "stop" reason to halt processing for that instrument/pipeline run.
*   7.4. **Layer 3 Modules: Analysis Modules (Signal Agents)** (`logic_type`: "agent")
    *   Examples: `ICT_Breakout_Agent_v1.py`, `SMC_FVG_Agent_v1.py`, `MeanReversion_Agent_v1.py`, `Reentry_Signal_Agent_v1.py`.
    *   Implement specific trading logic/pattern recognition using instrument data and context. Output potential trade signals/ideas (as dictionaries or simple objects) into a list within the `context_dict`. **Bespoke Python logic, minimal external frameworks.**
*   7.5. **Layer 4 Modules: Confluence Engine** (`logic_type`: "confluence")
    *   Examples: `Simple_Signal_Count_Confluence_v1.py`, `Weighted_Score_Confluence_v1.py`.
    *   Consume the list of signals/ideas generated by L3 agents. Apply aggregation, scoring, or filtering logic based on Config rules to identify high-probability setups. Output refined/confirmed trade ideas to `context_dict`.
*   7.6. **Layer 5 Modules: Risk Management & Execution Logic** (`logic_type`: "risk")
    *   Examples:
        *   `Dynamic_Risk_Allocator_v1.py`: Consumes market context, applies rules, sets dynamic risk params in `context_dict`.
        *   `Static_Risk_Per_Trade_Sizer_v1.py`: Calculates position size based on fixed risk %.
        *   `ATR_Stop_Loss_Setter_v1.py`: Calculates SL based on ATR.
        *   `Trade_Invalidation_Monitor_v1.py`: Checks conditions to invalidate an open idea/trade.
        *   `Basic_Scaling_Engine_v1.py`: Implements simple scale-out rules.
        *   `Trade_Idea_Manager_v1.py`: Potentially manages state of active ideas.
    *   Consume confirmed ideas and context (including dynamic risk params), calculate final execution parameters (size, SL, TP), manage aspects of the trade lifecycle (logging simulated actions). **Bespoke Python logic, critical validation needed.**
*   7.7. **Layer 6: Execution Interface** (Future Phase, `logic_type`: "execution")
    *   Examples: `CCXT_Order_Executor_v1.py`.
    *   Will consume final trade parameters from `context_dict`, translate them into exchange API calls (`CCXT`). Likely implemented as registered modules as well.
*   7.8. **Code Directory Structure (Example)**
    ```
    /corso-trader-ai/
    ├── main_orchestrator.py  # The core Python registry-driven runner
    ├── n8n_workflows/      # Exported n8n JSON workflows
    ├── src/                # Main Python code
    │   ├── modules/          # All registered logic modules
    │   │   ├── context/
    │   │   │   ├── __init__.py
    │   │   │   ├── market_state_analyzer_v1.py
    │   │   │   └── usdt_d_analyzer_v1.py
    │   │   ├── filters/
    │   │   │   └── volatility_filter_v1.py
    │   │   ├── agents/
    │   │   │   └── ict_breakout_agent_v1.py
    │   │   ├── confluence/
    │   │   │   └── simple_signal_count_confluence_v1.py
    │   │   └── risk/
    │   │       ├── dynamic_risk_allocator_v1.py
    │   │       └── static_risk_per_trade_sizer_v1.py
    │   ├── utils/            # Shared utilities (logging, db connection, etc.)
    │   │   ├── __init__.py
    │   │   ├── logging_config.py
    │   │   └── db_utils.py
    │   └── __init__.py
    ├── tests/              # Unit and integration tests
    │   ├── modules/
    │   │   └── context/
    │   │       └── test_market_state_analyzer_v1.py
    │   └── test_orchestrator.py
    ├── docs/               # Documentation
    │   ├── project_bible.md # This document
    │   └── context_dict_schema.md # CRITICAL I/O contract spec
    ├── requirements.txt    # Python dependencies
    ├── .gitignore
    └── README.md
    ```

**8. Data Management (Supabase - includes Module Registry)**

8.1. **`Module_Registry` Table (NEW & CRITICAL)**
    *   **Purpose:** Central inventory and configuration source for all executable logic blocks. The Python orchestrator relies entirely on this table.
    *   **Schema:**
        *   `module_id` (TEXT, PK, Unique, e.g., "usdt_d_analyzer_v1") - *Globally unique identifier.*
        *   `logic_type` (TEXT, NOT NULL, e.g., "context", "filter", "agent", "risk", "confluence", "execution") - *Categorization.*
        *   `version` (TEXT, NOT NULL, e.g., "1.0.0") - *Semantic versioning recommended.*
        *   `description` (TEXT) - *Human-readable purpose.*
        *   `script_path` (TEXT, NOT NULL, e.g., "src/modules/context/usdt_d_analyzer_v1.py") - *Relative path from project root.*
        *   `function_name` (TEXT, NOT NULL, e.g., "run_analysis") - *Entry function within the script.*
        *   `is_active` (BOOLEAN, NOT NULL, default: false) - *Controls if orchestrator can select this module.*
        *   `input_keys` (TEXT[], default: '{}') - *Array of required keys from `context_dict_schema.md`.*
        *   `output_keys` (TEXT[], default: '{}') - *Array of keys this module adds/modifies as per `context_dict_schema.md`.*
        *   `tags` (JSONB) - *Optional tags for filtering/grouping (e.g., {"strategy": "ICT", "asset_class": "crypto"}).*
        *   `created_at` (TIMESTAMPTZ, default: `now()`)
        *   `updated_at` (TIMESTAMPTZ, default: `now()`)
    *   **(Composite Unique Constraint suggested for `(logic_type, version, <name derived from module_id>)` if needed for easier querying/organization).**

8.2. **Configuration Tables (Referencing `module_id`)**
    *   **`Pipeline_Config`:** Defines ordered stages (e.g., 1: context, 2: filter...). May specify default `module_id`s to run per stage if no strategy-specific override exists.
    *   **`Strategy_Config`:** Maps a strategy name (e.g., "ICT_Scalper_v1") to specific sets or sequences of `module_id`s to be executed for certain pipeline stages, potentially overriding defaults. Allows running different combinations of modules as distinct strategies.
    *   **`Asset_Config`:** Configuration specific to assets (symbol, category, etc.). Could potentially override module choices or parameters for specific assets/categories.
    *   **`Risk_Config`:** Contains rules for risk management. Maps context signals (e.g., `market_regime`="risk_off") to risk parameters (`global_risk_multiplier`=0.25) or specifies parameters for specific risk `module_id`s. Uses JSONB heavily for flexibility.
    *   *The Python orchestrator queries these tables along with `Module_Registry` to dynamically determine the exact execution path and parameters.*

8.3. **Logging Tables (Including `module_id`/`version`)**
    *   **`Pipeline_Log`:** Records events during pipeline execution. Key Fields: `timestamp`, `run_id`, `stage`, **`module_id`**, **`module_version`**, `log_level`, `message`, **`rationale`** (text explaining *why* a decision was made), `context_snapshot` (JSONB of relevant `context_dict` state).
    *   **`Error_Log`:** Records errors during execution. Key Fields: `timestamp`, `run_id`, `stage`, **`module_id`** (if error within module), **`module_version`**, `error_message`, `traceback`, `context_snapshot`.

8.4. **Core Data Tables**
    *   `Instruments` (Symbol, base, quote, category, is_active, etc.)
    *   `Instrument_News` (Timestamp, symbol, source, headline, content snippet - *Phase 7+*)
    *   `Key_Levels` (Symbol, level, type, timestamp added, source module_id)
    *   `Trade_Ideas` (Timestamp generated, symbol, direction, entry_conditions, status, source_agent_module_id, confluence_module_id)
    *   `Trades` (Timestamp executed, symbol, direction, entry_price, size, initial_sl, initial_tp, status, idea_id, exit_price, exit_timestamp, pnl, risk_module_id, execution_module_id)
    *   `Performance_Ratings` (Timestamp, module_id, module_version, metric_name, value, context_snapshot - *Phase 6+*)

**9. Error Handling & Logging Strategy (Module-Aware)**

*   The main **Python orchestrator** implements top-level `try...except` blocks around the dynamic loading and execution calls for each module.
*   Errors are caught, logged comprehensively to `Error_Log` (including traceback, context state, and the failing `module_id`/`version`), and the orchestrator decides how to proceed (e.g., skip instrument, halt run).
*   Individual **modules** implement their own internal `try...except` blocks for specific operations (e.g., API calls, calculations) and use a shared logging utility (passed in or imported).
*   The **shared logging utility** standardizes log formats (JSON preferred), automatically includes metadata like timestamps, `run_id`, and crucially, allows easy injection of the current `module_id` and `module_version` into log records destined for `Pipeline_Log` or `Error_Log`.
*   **Input validation** (using Type Hints and explicit checks like Pydantic if warranted later) happens at the entry point of modules or the orchestrator to catch issues early.
*   **Rationale Logging:** Modules generating key decisions (filters blocking, agents signaling, risk modules sizing/invalidating) should explicitly log a human-readable `rationale` string explaining the *why* based on their inputs and logic.

**10. Phased Rollout Plan (Revised - Infrastructure First)**

*   **Phase 0: Setup & Core Infrastructure (2-4 weeks) - CRITICAL & INCREASED SCOPE**
    *   *Tasks:* Setup tools (Python, Git, VSCode/Cursor, n8n, Supabase account). Initialize Git repo. Define **`Module_Registry` schema** in Supabase & create table. Define **`context_dict_schema.md` (v1)** in `/docs`. Create basic Python module template (`hello_module_v1.py` - logs message, includes type hints, basic structure). Add entry for this module to `Module_Registry`. Create basic n8n workflow (manual trigger). **Implement the foundational Python orchestrator script (`main_orchestrator.py`)** capable of:
        1.  Connecting to Supabase (`supabase-py`, `db_utils.py`).
        2.  Reading a *single, specific* active module entry from `Module_Registry` based on `module_id`.
        3.  Dynamically importing the script (`script_path`) and executing the function (`function_name`).
        4.  Passing a basic `context_dict` and capturing minimal output.
        5.  Setting up basic shared logging (`logging_config.py`, `utils`) to write to console/file initially, including manual tagging of `module_id`.
        6.  Connect n8n workflow to execute this basic orchestrator script via `Execute Command`.
    *   **Success Criteria:** Base tools setup. Git repo active & pushed. `Module_Registry` table exists in Supabase with sample entry. `context_dict_schema.md` started. Basic orchestrator runs 1 sample module dynamically via registry lookup when triggered by n8n. Basic console/file logs produced by orchestrator and module.

*   **Phase 1: Robust Orchestrator & Logging (3-4 weeks)**
    *   *Tasks:* Enhance Python orchestrator to handle multiple sequential modules per *conceptual* stage (read multiple `module_id`s based on config/registry, loop execution). Implement robust Supabase logging via the shared utility, automatically tagging `module_id`/`version` in `Pipeline_Log` and `Error_Log`. Define basic `Pipeline_Config` table & logic in orchestrator to select modules per stage. Build 1 core **Context Module** (e.g., `Instrument_Loader_v1.py` - gets basic asset info). Register it. Configure pipeline via `Pipeline_Config` to run it. Update `context_dict` docs. Refine error handling in orchestrator.
    *   **Success Criteria:** Orchestrator dynamically runs multiple registered modules sequentially based on `Pipeline_Config`. Logging to Supabase `Pipeline_Log` / `Error_Log` is automated & correctly tagged. `Instruments` table usable by `Instrument_Loader`. Docs updated. Basic pipeline runs end-to-end logging module execution.

*   **Phase 2: Context Modules & Basic Filters (3-4 weeks)**
    *   *Tasks:* Build core **Context Modules** (L1 - e.g., `Session_Timing_v1`, `Market_State_Basic_v1`). Build 1-2 **Market Context Analyzer Modules** (L1 - e.g., `USDT_D_Basic_Analyzer_v1`). Build 1-2 simple **Filter Modules** (L2 - e.g., `Basic_Volume_Filter_v1`). Register all. Configure pipeline stages in `Pipeline_Config`. Update `context_dict` docs extensively.
    *   **Success Criteria:** Various context variables (time, market state, dominance trend) generated by modules and logged. Filters execute based on context via registry. Docs updated.

*   **Phase 3: Signal Agents & Basic Confluence/Risk (4-5 weeks)**
    *   *Tasks:* Build 1-2 **Signal Agent Modules** (L3 - bespoke Python, e.g., `Simple_Breakout_Agent_v1`). Build basic **Confluence Module** (L4 - e.g., `Require_N_Signals_Confluence_v1`). Build basic **Position Sizing Module** (L5 - fixed rules, e.g., `Fixed_Fractional_Sizer_v1`). Register all. Configure pipeline. Basic `Trade_Ideas`/`Trades` logging (simulated execution). Update docs.
    *   **Success Criteria:** Sized trade ideas proposed & logged via dynamically loaded modules. Basic confluence logic applied. Docs updated.

*   **Phase 4: Dynamic Risk & Reentry Logic (4-5 weeks) - COMPLEXITY JUMP**
    *   *Tasks:* Define `Risk_Config` table structure. Implement **`Dynamic_Risk_Allocator` Module** (L5) consuming market context signals & `Risk_Config` rules. Build **`Reentry_Signal_Agent` Module** (L3). Enhance Confluence/Risk flow to handle reentry ideas. Register/Configure. Build more L3 agents. Update docs.
    *   **Success Criteria:** Risk allocation (e.g., sizing multiplier) adjusts based on market context signals read from `context_dict` and rules from `Risk_Config`. Reentry logic simulated correctly via modules. Docs updated.

*   **Phase 5: Scaling & Invalidation Modules (4-5 weeks)**
    *   *Tasks:* Implement **Scaling Modules** (L5 - e.g., `ATR_Trailing_Stop_v1`, `Take_Profit_Zone_v1`). Implement **Invalidation Modules** (L5 - e.g., `Structure_Break_Invalidation_v1`). Register/Configure. Refine schemas. Establish `Performance_Ratings` schema. Update docs.
    *   **Success Criteria:** Simple scaling/invalidation logic simulated correctly via registered modules. Docs updated.

*   **Phase 6: Backtesting & Parameter Tuning (4-6 weeks)**
    *   *Tasks:* **Implement/Integrate Backtesting framework.** Critically, this framework *must* use the **same Python orchestrator and registry mechanism** to run historical data through the configured pipeline modules. Evaluate simple custom loop vs. adapting lightweight OSS tools. Run backtests extensively. Populate `Performance_Ratings` table based on module contribution to trades. Tune parameters (in Config tables, including `Risk_Config` rules, module selection in `Strategy_Config`).
    *   **Success Criteria:** Reliable backtesting completed using the registry-driven pipeline. Initial performance ratings generated per module/version. Parameters tuned via config updates. Backtesting approach documented.

*   **Phase 7+: Advanced Features & Live Simulation (Ongoing)**
    *   *Tasks:* Add more sophisticated modules (Agents, Confluence, Risk). Implement dynamic signal weighting (L4) based on `Performance_Ratings`. Full *Dynamic Scaling In/Out* module (L5). News Feed module (`feedparser`, L1/L3). Integrate `transformers` for sentiment module (L1/L3) if desired. Build Layer 6 execution modules (`CCXT`) for paper trading simulation via the orchestrator. Build Performance Analysis module (reading logs/ratings).
    *   **Success Criteria:** Advanced features integrated as modules. Paper trading operational and driven by the orchestrator/registry. Performance analysis yields actionable insights.

**11. Development Workflow & AI Collaboration Strategy (Registry Focus)**

*   Use Git frequently (feature branches recommended). Follow Phased Plan & Success Criteria. Adhere strictly to **Module Creation Workflow**.
*   Maintain **`Module_Registry`** entries meticulously.
*   Maintain **`context_dict_schema.md`** rigorously – it's the API contract.
*   Maintain **Prompt Library** for generating module code, unit tests, registry entry details, schema updates.
*   Use Mini-Projects/Testing per module. Prioritize clear AI communication. Review AI code.

**12. Non-Negotiables & Core Tenets (Registry Integrity)**

*   Risk limits unbreakable. Path-aware/Module-tagged logging with rationale. Documented `context_dict` & enforced contracts. Modularity via Registry. **Registry is Source of Truth.** Config in Supabase. Understand AI code. Adhere to Plan. Use **UTC** consistently. Test thoroughly (Unit, Integration, Backtesting). **Type Hints.** **Input Validation.** **Maintain Registry and Schema Integrity absolutely.**

**13. Risks & Mitigation Strategies (Includes Infrastructure Complexity)**

1.  **Complexity Overwhelm (VERY HIGH initially):** *Mitigation:* **Prioritize building & stabilizing core registry/orchestrator infrastructure in Phase 0/1.** Strict adherence to Phased Plan, Module Workflow, unit tests per module, AI assist, start modules simply, clear Success Criteria per phase. Break down complex modules.
2.  **Infrastructure Implementation Errors (NEW - HIGH):** *Mitigation:* Dedicated focus in early phases (0/1), thorough testing of the orchestrator's dynamic loading, registry querying, and context passing logic, clear utility functions (DB, logging), code reviews (AI/self), start with simple module structures.
3.  **Implementation Errors (Modules - HIGH):** *Mitigation:* Unit testing, Input Validation, Type Hints, adherence to `context_dict` contract, templates, logging within modules, AI code reviews, backtesting.
4.  **Configuration Errors (NEW - MEDIUM):** *Mitigation:* Clear configuration schemas, validation scripts/checks before activating complex strategies, careful management of `Module_Registry` active status and config table references, versioning.
5.  **Data Quality/API Issues (MEDIUM):** *Mitigation:* Health checks (in L0 or L1 modules), reputable sources (CCXT), redundancy/fallbacks where possible, error handling in data-consuming modules.
6.  **Overfitting (MEDIUM):** *Mitigation:* Out-of-sample backtesting, walk-forward testing, evaluating performance across different market regimes (using context modules), focus on robust signals over curve-fitting, parameter sensitivity analysis.
7.  **AI Over-Reliance (MEDIUM):** *Mitigation:* Actively understand generated code, focused learning sprints on Python/Pandas/etc., rigorous testing and debugging, treating AI as a powerful assistant, not an infallible oracle.
8.  **Cost Overruns (MEDIUM):** *Mitigation:* Implement Cost Optimization practices (prompt efficiency, caching data locally/in simple storage if feasible, monitor Supabase/Render usage, set alerts, stay within reasonable free/low-cost tiers, prioritize core features).
9.  **Scope Creep (HIGH):** *Mitigation:* Stick brutally to the Phased Plan & Success Criteria per phase. Use a backlog for future ideas *not* to be implemented now. Evaluate all new features against the registry/module architecture – does it fit cleanly?
10. **Motivation/Burnout (MEDIUM):** *Mitigation:* Celebrate phase completions, focus on learning, take breaks, keep a journal of progress/challenges, break down large tasks, ensure tests provide quick feedback loops.
11. **OSS Integration Risks (MEDIUM):** *Mitigation:* Selective adoption (commodity tasks only), avoid core logic frameworks, sandbox testing, check license/activity, use AI for integration help but *own* the validation.

---
**(End of Project Bible v4.5)**