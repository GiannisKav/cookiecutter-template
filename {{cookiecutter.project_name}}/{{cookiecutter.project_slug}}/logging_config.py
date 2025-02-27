import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from loguru import logger


def setup_logger(
    process_name: Optional[str] = None,
    log_file_path: Optional[Union[os.PathLike, str]] = None,
    log_file_dir: Optional[Union[os.PathLike, str]] = None,
    log_level: str = "INFO",
) -> None:
    # Remove default sink
    logger.remove()

    # Add console logger
    logger.add(
        sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level=log_level.upper(),
    )

    if log_file_path is not None:
        # Ensure directory exists
        Path(log_file_path).parent.mkdir(parents=True, exist_ok=True)

        # Add file logger
        logger.add(
            str(log_file_path),
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level=log_level.upper(),
        )
    elif log_file_dir is not None:
        # Ensure directory exists
        log_file_dir = Path(log_file_dir)
        log_file_dir.mkdir(parents=True, exist_ok=True)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        if process_name is None:
            logs_path = log_file_dir / f"{current_time}.log"
        else:
            logs_path = log_file_dir / f"{process_name}_{current_time}.log"
        # Add file logger
        logger.add(
            str(logs_path),
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level=log_level.upper(),
        )
