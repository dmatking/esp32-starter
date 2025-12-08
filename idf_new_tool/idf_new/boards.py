# Copyright 2025 David M. King
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from .paths import BOARDS_DIR


BOARD_IMPL = "board_impl.c"


def _board_dirs() -> list[Path]:
    if not BOARDS_DIR.exists():
        return []
    return sorted(
        impl.parent for impl in BOARDS_DIR.rglob(BOARD_IMPL) if impl.is_file()
    )


def list_boards() -> list[str]:
    """Return board IDs relative to boards/ (supports nested folders)."""
    return [directory.relative_to(BOARDS_DIR).as_posix() for directory in _board_dirs()]


def _ensure_within_boards(path: Path) -> None:
    try:
        path.relative_to(BOARDS_DIR.resolve())
    except ValueError as exc:  # pragma: no cover - defensive guardrail
        raise SystemExit("Board path escapes boards/ directory") from exc


def validate_board(board_id: str) -> Path:
    candidate = (BOARDS_DIR / board_id).resolve()
    _ensure_within_boards(candidate)
    if not candidate.exists() or not candidate.is_dir():
        available = list_boards()
        raise SystemExit(
            f"Board '{board_id}' not found.\nAvailable boards: {', '.join(available)}"
        )
    board_impl = candidate / BOARD_IMPL
    if not board_impl.exists():
        raise SystemExit(f"Board '{board_id}' is missing {BOARD_IMPL}")
    return candidate
