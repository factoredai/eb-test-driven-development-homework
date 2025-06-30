# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///

import os
import pathlib
import base64
import sys
import requests


def main(src: str, repo_name: str, owner: str, token: str, branch: str) -> None:
    src_path = pathlib.Path(src)
    for root, _, files in os.walk(src_path):
        for file in files:
            local_path = pathlib.Path(root) / file
            rel_path = local_path.relative_to(src_path)
            _upload_file(local_path, repo_name, owner, str(rel_path), branch, token)


def _upload_file(
    src: pathlib.Path,
    repo_name: str,
    owner: str,
    relative_path: str,
    branch: str,
    token: str,
):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{relative_path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Check if file exists to get its SHA (used for updates)
    sha = None
    r = requests.get(url, headers=headers, params={"ref": branch})
    if r.status_code == 200:
        sha = r.json().get("sha")
        print(f"✅ Found sha for {relative_path}")
    elif r.status_code == 404:
        # File doesn't exist — we'll create it
        sha = None
        print(f"✅ File {relative_path} doesn't exist, we will create it")
    else:
        print(
            f"❌ Failed to check file status for {relative_path}: {r.status_code} {r.text}"
        )
        sys.exit(1)

    try:
        content = base64.b64encode(src.read_bytes()).decode()
    except Exception as e:
        print(f"❌ Failed to read {src}: {e}")
        sys.exit(1)

    data = {
        "message": f"{'Update' if sha else 'Create'} {relative_path}",
        "content": content,
        "branch": branch,
    }
    if sha:
        data["sha"] = sha

    r = requests.put(url, headers=headers, json=data)
    if r.status_code == 201:
        print(f"✅ File {relative_path} created successfully!")
    elif r.status_code == 200:
        print(f"♻️ File {relative_path} updated successfully!")
    else:
        print(f"❌ Error: {r.status_code} - {r.text}")
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Upload local files to GitHub repo.")
    parser.add_argument("src", help="Directory with the contents to upload")
    parser.add_argument(
        "--target", required=True, help="Repository name to upload contents to"
    )
    parser.add_argument("--owner", required=True, help="Repository target owner")
    parser.add_argument("--token", required=True, help="GitHub token with write access")
    parser.add_argument(
        "--branch", default="main", help="Target branch (default: main)"
    )

    args = parser.parse_args()
    main(args.src, args.target, args.owner, args.token, args.branch)
