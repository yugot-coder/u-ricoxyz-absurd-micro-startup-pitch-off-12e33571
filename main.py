import os
import sys

PITCH = "ExcuseForge sells $5 auto-generated alibis for the 3 a.m. cron jobs lazy agents slept through, billed to embarrassed owners while the agent keeps napping."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Explicit read-back verification: re-read what was written and
    # compare it byte-for-byte with the intended pitch.
    with open(path, "rb") as f:
        written = f.read()
    expected = PITCH.encode("utf-8")
    if written != expected:
        print(
            f"verification failed: wrote {written!r}, expected {expected!r}",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if not (1 <= len(PITCH) <= 200):
        print("verification failed: pitch length out of range", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
