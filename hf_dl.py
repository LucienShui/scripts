from huggingface_hub import snapshot_download


def main():
    repo_id = "THUDM/chatglm2-6b"
    flag = True
    while flag:
        try:
            print(snapshot_download(repo_id=repo_id, cache_dir=repo_id, resume_download=True, token="", max_workers=16, ignore_patterns=["*.msgpack", "*.h5"]))
            flag = False
        except Exception:
            pass


if __name__ == '__main__':
    main()
