from _typeshed import Incomplete
from camel.types.unified_model_type import UnifiedModelType
from enum import Enum, EnumMeta

logger: Incomplete

class RoleType(Enum):
    ASSISTANT: str
    USER: str
    CRITIC: str
    EMBODIMENT: str
    DEFAULT: str

class ModelType(UnifiedModelType, Enum):
    DEFAULT: Incomplete
    GPT_3_5_TURBO: str
    GPT_4: str
    GPT_4_TURBO: str
    GPT_4O: str
    GPT_4O_MINI: str
    GPT_4_5_PREVIEW: str
    O1: str
    O1_PREVIEW: str
    O1_MINI: str
    O3_MINI: str
    GPT_4_1: str
    GPT_4_1_MINI: str
    GPT_4_1_NANO: str
    O4_MINI: str
    O3: str
    AWS_CLAUDE_3_7_SONNET: str
    AWS_CLAUDE_3_5_SONNET: str
    AWS_CLAUDE_3_HAIKU: str
    AWS_CLAUDE_3_SONNET: str
    AWS_DEEPSEEK_R1: str
    AWS_LLAMA_3_3_70B_INSTRUCT: str
    AWS_LLAMA_3_2_90B_INSTRUCT: str
    AWS_LLAMA_3_2_11B_INSTRUCT: str
    GLM_4: str
    GLM_4V: str
    GLM_4V_FLASH: str
    GLM_4V_PLUS_0111: str
    GLM_4_PLUS: str
    GLM_4_AIR: str
    GLM_4_AIR_0111: str
    GLM_4_AIRX: str
    GLM_4_LONG: str
    GLM_4_FLASHX: str
    GLM_4_FLASH: str
    GLM_ZERO_PREVIEW: str
    GLM_3_TURBO: str
    GROQ_LLAMA_3_1_8B: str
    GROQ_LLAMA_3_3_70B: str
    GROQ_LLAMA_3_3_70B_PREVIEW: str
    GROQ_LLAMA_3_8B: str
    GROQ_LLAMA_3_70B: str
    GROQ_MIXTRAL_8_7B: str
    GROQ_GEMMA_2_9B_IT: str
    OPENROUTER_LLAMA_3_1_405B: str
    OPENROUTER_LLAMA_3_1_70B: str
    OPENROUTER_LLAMA_4_MAVERICK: str
    OPENROUTER_LLAMA_4_MAVERICK_FREE: str
    OPENROUTER_LLAMA_4_SCOUT: str
    OPENROUTER_LLAMA_4_SCOUT_FREE: str
    OPENROUTER_OLYMPICODER_7B: str
    LMSTUDIO_GEMMA_3_1B: str
    LMSTUDIO_GEMMA_3_4B: str
    LMSTUDIO_GEMMA_3_12B: str
    LMSTUDIO_GEMMA_3_27B: str
    TOGETHER_LLAMA_3_1_8B: str
    TOGETHER_LLAMA_3_1_70B: str
    TOGETHER_LLAMA_3_1_405B: str
    TOGETHER_LLAMA_3_3_70B: str
    TOGETHER_MIXTRAL_8_7B: str
    TOGETHER_MISTRAL_7B: str
    TOGETHER_LLAMA_4_MAVERICK: str
    TOGETHER_LLAMA_4_SCOUT: str
    PPIO_DEEPSEEK_PROVER_V2_671B: str
    PPIO_DEEPSEEK_R1_TURBO: str
    PPIO_DEEPSEEK_V3_TURBO: str
    PPIO_DEEPSEEK_R1_COMMUNITY: str
    PPIO_DEEPSEEK_V3_COMMUNITY: str
    PPIO_DEEPSEEK_R1: str
    PPIO_DEEPSEEK_V3: str
    PPIO_QWEN_2_5_72B: str
    PPIO_BAICHUAN_2_13B_CHAT: str
    PPIO_LLAMA_3_3_70B: str
    PPIO_LLAMA_3_1_70B: str
    PPIO_YI_1_5_34B_CHAT: str
    SAMBA_LLAMA_3_1_8B: str
    SAMBA_LLAMA_3_1_70B: str
    SAMBA_LLAMA_3_1_405B: str
    SGLANG_LLAMA_3_1_8B: str
    SGLANG_LLAMA_3_1_70B: str
    SGLANG_LLAMA_3_1_405B: str
    SGLANG_LLAMA_3_2_1B: str
    SGLANG_MIXTRAL_NEMO: str
    SGLANG_MISTRAL_7B: str
    SGLANG_QWEN_2_5_7B: str
    SGLANG_QWEN_2_5_32B: str
    SGLANG_QWEN_2_5_72B: str
    STUB: str
    CLAUDE_2_1: str
    CLAUDE_2_0: str
    CLAUDE_INSTANT_1_2: str
    CLAUDE_3_OPUS: str
    CLAUDE_3_SONNET: str
    CLAUDE_3_HAIKU: str
    CLAUDE_3_5_SONNET: str
    CLAUDE_3_5_HAIKU: str
    CLAUDE_3_7_SONNET: str
    NETMIND_LLAMA_4_MAVERICK_17B_128E_INSTRUCT: str
    NETMIND_LLAMA_4_SCOUT_17B_16E_INSTRUCT: str
    NETMIND_DEEPSEEK_R1: str
    NETMIND_DEEPSEEK_V3: str
    NETMIND_DOUBAO_1_5_PRO: str
    NETMIND_QWQ_32B: str
    NVIDIA_NEMOTRON_340B_INSTRUCT: str
    NVIDIA_NEMOTRON_340B_REWARD: str
    NVIDIA_YI_LARGE: str
    NVIDIA_MISTRAL_LARGE: str
    NVIDIA_MIXTRAL_8X7B: str
    NVIDIA_LLAMA3_70B: str
    NVIDIA_LLAMA3_1_8B_INSTRUCT: str
    NVIDIA_LLAMA3_1_70B_INSTRUCT: str
    NVIDIA_LLAMA3_1_405B_INSTRUCT: str
    NVIDIA_LLAMA3_2_1B_INSTRUCT: str
    NVIDIA_LLAMA3_2_3B_INSTRUCT: str
    NVIDIA_LLAMA3_3_70B_INSTRUCT: str
    GEMINI_2_5_PRO_EXP: str
    GEMINI_2_0_FLASH: str
    GEMINI_2_0_FLASH_THINKING: str
    GEMINI_2_0_PRO_EXP: str
    GEMINI_2_0_FLASH_LITE_PREVIEW: str
    GEMINI_1_5_FLASH: str
    GEMINI_1_5_PRO: str
    MISTRAL_3B: str
    MISTRAL_7B: str
    MISTRAL_8B: str
    MISTRAL_CODESTRAL: str
    MISTRAL_CODESTRAL_MAMBA: str
    MISTRAL_LARGE: str
    MISTRAL_MIXTRAL_8x7B: str
    MISTRAL_MIXTRAL_8x22B: str
    MISTRAL_NEMO: str
    MISTRAL_PIXTRAL_12B: str
    MISTRAL_MEDIUM_3: str
    REKA_CORE: str
    REKA_FLASH: str
    REKA_EDGE: str
    COHERE_COMMAND_R_PLUS: str
    COHERE_COMMAND_R: str
    COHERE_COMMAND_LIGHT: str
    COHERE_COMMAND: str
    COHERE_COMMAND_NIGHTLY: str
    QWEN_MAX: str
    QWEN_PLUS: str
    QWEN_TURBO: str
    QWEN_PLUS_LATEST: str
    QWEN_PLUS_2025_04_28: str
    QWEN_TURBO_LATEST: str
    QWEN_TURBO_2025_04_28: str
    QWEN_LONG: str
    QWEN_VL_MAX: str
    QWEN_VL_PLUS: str
    QWEN_MATH_PLUS: str
    QWEN_MATH_TURBO: str
    QWEN_CODER_TURBO: str
    QWEN_2_5_CODER_32B: str
    QWEN_2_5_VL_72B: str
    QWEN_2_5_72B: str
    QWEN_2_5_32B: str
    QWEN_2_5_14B: str
    QWEN_QWQ_32B: str
    QWEN_QVQ_72B: str
    QWEN_QWQ_PLUS: str
    YI_LIGHTNING: str
    YI_LARGE: str
    YI_MEDIUM: str
    YI_LARGE_TURBO: str
    YI_VISION: str
    YI_MEDIUM_200K: str
    YI_SPARK: str
    YI_LARGE_RAG: str
    YI_LARGE_FC: str
    DEEPSEEK_CHAT: str
    DEEPSEEK_REASONER: str
    INTERNLM3_LATEST: str
    INTERNLM3_8B_INSTRUCT: str
    INTERNLM2_5_LATEST: str
    INTERNLM2_PRO_CHAT: str
    MOONSHOT_V1_8K: str
    MOONSHOT_V1_32K: str
    MOONSHOT_V1_128K: str
    SILICONFLOW_DEEPSEEK_V2_5: str
    SILICONFLOW_DEEPSEEK_V3: str
    SILICONFLOW_INTERN_LM2_5_20B_CHAT: str
    SILICONFLOW_INTERN_LM2_5_7B_CHAT: str
    SILICONFLOW_PRO_INTERN_LM2_5_7B_CHAT: str
    SILICONFLOW_QWEN2_5_72B_INSTRUCT: str
    SILICONFLOW_QWEN2_5_32B_INSTRUCT: str
    SILICONFLOW_QWEN2_5_14B_INSTRUCT: str
    SILICONFLOW_QWEN2_5_7B_INSTRUCT: str
    SILICONFLOW_PRO_QWEN2_5_7B_INSTRUCT: str
    SILICONFLOW_THUDM_GLM_4_9B_CHAT: str
    SILICONFLOW_PRO_THUDM_GLM_4_9B_CHAT: str
    AIML_MIXTRAL_8X7B: str
    AIML_MISTRAL_7B_INSTRUCT: str
    NOVITA_LLAMA_4_MAVERICK_17B: str
    NOVITA_LLAMA_4_SCOUT_17B: str
    NOVITA_DEEPSEEK_V3_0324: str
    NOVITA_QWEN_2_5_V1_72B: str
    NOVITA_DEEPSEEK_V3_TURBO: str
    NOVITA_DEEPSEEK_R1_TURBO: str
    NOVITA_GEMMA_3_27B_IT: str
    NOVITA_QWEN_32B: str
    NOVITA_L3_8B_STHENO_V3_2: str
    NOVITA_MYTHOMAX_L2_13B: str
    NOVITA_DEEPSEEK_R1_DISTILL_LLAMA_8B: str
    NOVITA_DEEPSEEK_V3: str
    NOVITA_LLAMA_3_1_8B: str
    NOVITA_DEEPSEEK_R1_DISTILL_QWEN_14B: str
    NOVITA_LLAMA_3_3_70B: str
    NOVITA_QWEN_2_5_72B: str
    NOVITA_MISTRAL_NEMO: str
    NOVITA_DEEPSEEK_R1_DISTILL_QWEN_32B: str
    NOVITA_LLAMA_3_8B: str
    NOVITA_WIZARDLM_2_8X22B: str
    NOVITA_DEEPSEEK_R1_DISTILL_LLAMA_70B: str
    NOVITA_LLAMA_3_1_70B: str
    NOVITA_GEMMA_2_9B_IT: str
    NOVITA_MISTRAL_7B: str
    NOVITA_LLAMA_3_70B: str
    NOVITA_DEEPSEEK_R1: str
    NOVITA_HERMES_2_PRO_LLAMA_3_8B: str
    NOVITA_L3_70B_EURYALE_V2_1: str
    NOVITA_DOLPHIN_MIXTRAL_8X22B: str
    NOVITA_AIROBOROS_L2_70B: str
    NOVITA_MIDNIGHT_ROSE_70B: str
    NOVITA_L3_8B_LUNARIS: str
    NOVITA_GLM_4_9B_0414: str
    NOVITA_GLM_Z1_9B_0414: str
    NOVITA_GLM_Z1_32B_0414: str
    NOVITA_GLM_4_32B_0414: str
    NOVITA_GLM_Z1_RUMINATION_32B_0414: str
    NOVITA_QWEN_2_5_7B: str
    NOVITA_LLAMA_3_2_1B: str
    NOVITA_LLAMA_3_2_11B_VISION: str
    NOVITA_LLAMA_3_2_3B: str
    NOVITA_LLAMA_3_1_8B_BF16: str
    NOVITA_L31_70B_EURYALE_V2_2: str
    MODELSCOPE_QWEN_2_5_7B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_14B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_32B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_72B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_CODER_7B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_CODER_14B_INSTRUCT: str
    MODELSCOPE_QWEN_2_5_CODER_32B_INSTRUCT: str
    MODELSCOPE_QWEN_3_235B_A22B: str
    MODELSCOPE_QWEN_3_32B: str
    MODELSCOPE_QWQ_32B: str
    MODELSCOPE_QWQ_32B_PREVIEW: str
    MODELSCOPE_LLAMA_3_1_8B_INSTRUCT: str
    MODELSCOPE_LLAMA_3_1_70B_INSTRUCT: str
    MODELSCOPE_LLAMA_3_1_405B_INSTRUCT: str
    MODELSCOPE_LLAMA_3_3_70B_INSTRUCT: str
    MODELSCOPE_MINISTRAL_8B_INSTRUCT: str
    MODELSCOPE_DEEPSEEK_V3_0324: str
    WATSONX_GRANITE_3_8B_INSTRUCT: str
    WATSONX_LLAMA_3_3_70B_INSTRUCT: str
    WATSONX_LLAMA_3_2_1B_INSTRUCT: str
    WATSONX_LLAMA_3_2_3B_INSTRUCT: str
    WATSONX_LLAMA_3_2_11B_VISION_INSTRUCT: str
    WATSONX_LLAMA_3_2_90B_VISION_INSTRUCT: str
    WATSONX_LLAMA_GUARD_3_11B_VISION_INSTRUCT: str
    WATSONX_MISTRAL_LARGE: str
    def __new__(cls, value) -> ModelType: ...
    @classmethod
    def from_name(cls, name): ...
    @property
    def value_for_tiktoken(self) -> str: ...
    @property
    def support_native_structured_output(self) -> bool: ...
    @property
    def support_native_tool_calling(self) -> bool: ...
    @property
    def is_openai(self) -> bool: ...
    @property
    def is_aws_bedrock(self) -> bool: ...
    @property
    def is_azure_openai(self) -> bool: ...
    @property
    def is_zhipuai(self) -> bool: ...
    @property
    def is_anthropic(self) -> bool: ...
    @property
    def is_groq(self) -> bool: ...
    @property
    def is_openrouter(self) -> bool: ...
    @property
    def is_lmstudio(self) -> bool: ...
    @property
    def is_together(self) -> bool: ...
    @property
    def is_sambanova(self) -> bool: ...
    @property
    def is_mistral(self) -> bool: ...
    @property
    def is_nvidia(self) -> bool: ...
    @property
    def is_gemini(self) -> bool: ...
    @property
    def is_reka(self) -> bool: ...
    @property
    def is_cohere(self) -> bool: ...
    @property
    def is_yi(self) -> bool: ...
    @property
    def is_qwen(self) -> bool: ...
    @property
    def is_deepseek(self) -> bool: ...
    @property
    def is_netmind(self) -> bool: ...
    @property
    def is_ppio(self) -> bool: ...
    @property
    def is_internlm(self) -> bool: ...
    @property
    def is_modelscope(self) -> bool: ...
    @property
    def is_moonshot(self) -> bool: ...
    @property
    def is_sglang(self) -> bool: ...
    @property
    def is_siliconflow(self) -> bool: ...
    @property
    def is_watsonx(self) -> bool: ...
    @property
    def is_novita(self) -> bool: ...
    @property
    def is_aiml(self) -> bool: ...
    @property
    def token_limit(self) -> int: ...

class EmbeddingModelType(Enum):
    TEXT_EMBEDDING_ADA_2: str
    TEXT_EMBEDDING_3_SMALL: str
    TEXT_EMBEDDING_3_LARGE: str
    JINA_EMBEDDINGS_V3: str
    JINA_CLIP_V2: str
    JINA_COLBERT_V2: str
    JINA_EMBEDDINGS_V2_BASE_CODE: str
    MISTRAL_EMBED: str
    GEMINI_EMBEDDING_EXP: str
    @property
    def is_openai(self) -> bool: ...
    @property
    def is_jina(self) -> bool: ...
    @property
    def is_mistral(self) -> bool: ...
    @property
    def is_gemini(self) -> bool: ...
    @property
    def output_dim(self) -> int: ...

class GeminiEmbeddingTaskType(str, Enum):
    SEMANTIC_SIMILARITY: str
    CLASSIFICATION: str
    CLUSTERING: str
    RETRIEVAL_DOCUMENT: str
    RETRIEVAL_QUERY: str
    QUESTION_ANSWERING: str
    FACT_VERIFICATION: str
    CODE_RETRIEVAL_QUERY: str

class TaskType(Enum):
    AI_SOCIETY: str
    CODE: str
    MISALIGNMENT: str
    TRANSLATION: str
    EVALUATION: str
    SOLUTION_EXTRACTION: str
    ROLE_DESCRIPTION: str
    GENERATE_TEXT_EMBEDDING_DATA: str
    OBJECT_RECOGNITION: str
    IMAGE_CRAFT: str
    MULTI_CONDITION_IMAGE_CRAFT: str
    DEFAULT: str
    VIDEO_DESCRIPTION: str

class VectorDistance(Enum):
    DOT: str
    COSINE: str
    EUCLIDEAN: str

class OpenAIBackendRole(Enum):
    ASSISTANT: str
    SYSTEM: str
    DEVELOPER: str
    USER: str
    FUNCTION: str
    TOOL: str

class TerminationMode(Enum):
    ANY: str
    ALL: str

class OpenAIImageTypeMeta(EnumMeta):
    def __contains__(cls, image_type: object) -> bool: ...

class OpenAIImageType(Enum, metaclass=OpenAIImageTypeMeta):
    PNG: str
    JPEG: str
    JPG: str
    WEBP: str
    GIF: str

class OpenAIVisionDetailType(Enum):
    AUTO: str
    LOW: str
    HIGH: str

class StorageType(Enum):
    MILVUS: str
    QDRANT: str
    TIDB: str

class OpenAPIName(Enum):
    COURSERA: str
    KLARNA: str
    SPEAK: str
    NASA_APOD: str
    BIZTOC: str
    CREATE_QR_CODE: str
    OUTSCHOOL: str
    WEB_SCRAPER: str

class ModelPlatformType(Enum):
    DEFAULT: Incomplete
    OPENAI: str
    AWS_BEDROCK: str
    AZURE: str
    ANTHROPIC: str
    GROQ: str
    OPENROUTER: str
    OLLAMA: str
    LITELLM: str
    LMSTUDIO: str
    ZHIPU: str
    GEMINI: str
    VLLM: str
    MISTRAL: str
    REKA: str
    TOGETHER: str
    STUB: str
    OPENAI_COMPATIBLE_MODEL: str
    SAMBA: str
    COHERE: str
    YI: str
    QWEN: str
    NVIDIA: str
    DEEPSEEK: str
    PPIO: str
    SGLANG: str
    INTERNLM: str
    MOONSHOT: str
    MODELSCOPE: str
    SILICONFLOW: str
    AIML: str
    VOLCANO: str
    NETMIND: str
    NOVITA: str
    WATSONX: str
    @classmethod
    def from_name(cls, name): ...
    @property
    def is_openai(self) -> bool: ...
    @property
    def is_aws_bedrock(self) -> bool: ...
    @property
    def is_azure(self) -> bool: ...
    @property
    def is_anthropic(self) -> bool: ...
    @property
    def is_groq(self) -> bool: ...
    @property
    def is_openrouter(self) -> bool: ...
    @property
    def is_lmstudio(self) -> bool: ...
    @property
    def is_ollama(self) -> bool: ...
    @property
    def is_vllm(self) -> bool: ...
    @property
    def is_sglang(self) -> bool: ...
    @property
    def is_together(self) -> bool: ...
    @property
    def is_litellm(self) -> bool: ...
    @property
    def is_zhipuai(self) -> bool: ...
    @property
    def is_mistral(self) -> bool: ...
    @property
    def is_openai_compatible_model(self) -> bool: ...
    @property
    def is_gemini(self) -> bool: ...
    @property
    def is_reka(self) -> bool: ...
    @property
    def is_samba(self) -> bool: ...
    @property
    def is_cohere(self) -> bool: ...
    @property
    def is_yi(self) -> bool: ...
    @property
    def is_qwen(self) -> bool: ...
    @property
    def is_nvidia(self) -> bool: ...
    @property
    def is_deepseek(self) -> bool: ...
    @property
    def is_netmind(self) -> bool: ...
    @property
    def is_ppio(self) -> bool: ...
    @property
    def is_internlm(self) -> bool: ...
    @property
    def is_moonshot(self) -> bool: ...
    @property
    def is_modelscope(self) -> bool: ...
    @property
    def is_siliconflow(self) -> bool: ...
    @property
    def is_aiml(self) -> bool: ...
    @property
    def is_volcano(self) -> bool: ...
    @property
    def is_novita(self) -> bool: ...
    @property
    def is_watsonx(self) -> bool: ...

class AudioModelType(Enum):
    TTS_1: str
    TTS_1_HD: str
    @property
    def is_openai(self) -> bool: ...

class VoiceType(Enum):
    ALLOY: str
    ECHO: str
    FABLE: str
    ONYX: str
    NOVA: str
    SHIMMER: str
    @property
    def is_openai(self) -> bool: ...

class JinaReturnFormat(Enum):
    DEFAULT: Incomplete
    MARKDOWN: str
    HTML: str
    TEXT: str

class HuggingFaceRepoType(str, Enum):
    DATASET: str
    MODEL: str
    SPACE: str
