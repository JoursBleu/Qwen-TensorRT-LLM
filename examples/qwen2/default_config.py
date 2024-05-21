import os


class DefaultConfig:
    now_dir = os.path.dirname(os.path.abspath(__file__))
    # hf_model_dir = os.path.join(now_dir, "qwen1.5_7b_chat")
    # tokenizer_dir = os.path.join(now_dir, "qwen1.5_7b_chat")
    # int4_gptq_model_dir = os.path.join(now_dir, "qwen1.5_7b_chat_int4")
    # ft_dir_path = os.path.join(now_dir, "c-model", "qwen1.5_7b_chat")
    # engine_dir = os.path.join(now_dir, "trt_engines", "fp16", "1-gpu")
    
    hf_model_dir = '/lpai/volumes/cloudmodel-muses/yuxiaoyang/llava_qwen4b_sft_v4.5_onlyqwen2'
    tokenizer_dir = '/lpai/volumes/cloudmodel-muses/yuxiaoyang/llava_qwen4b_sft_v4.5_onlyqwen2'
    int4_gptq_model_dir = os.path.join(now_dir, "qwen1.5_7b_chat_int4")
    ft_dir_path = '/lpai/volumes/lpai-demo-muses/xiaoyang/trt_engines/llava_qwen4b/smoothquant_models'
    # engine_dir = '/lpai/volumes/lpai-demo-muses/xiaoyang/trt_engines/llava_qwen4b/trtllm080/smoothquant/trt_engines/lpex_engine'
    # engine_dir = '/lpai/volumes/lpai-demo-muses/xiaoyang/trt_engines/qwen1.5/4b/trtllm080/int8_weight_only/1gpu'
    engine_dir = '/lpai/volumes/lpai-demo-muses/xiaoyang/trt_engines/llava_qwen4b/trtllm080_1/int8_weight_only/1gpu'
    # Maximum batch size for HF backend.
    hf_max_batch_size = 16

    # Maximum batch size for TRT-LLM backend.
    trt_max_batch_size = 16

    # choice the model format, base or chat
    #  choices=["chatml", "raw"],
    chat_format = "chatml"

    # Maximum input length.
    max_input_len = 1024 * 2

    # Maximum number of generate new tokens.
    max_new_tokens = 512 * trt_max_batch_size

    max_output_len = max_new_tokens

    # Top p for sampling.
    top_p = 0.8

    # Top k for sampling.
    top_k = 50

    # Temperature for sampling.
    temperature = 1.0


default_config = DefaultConfig()
