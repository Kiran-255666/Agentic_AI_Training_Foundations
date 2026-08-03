import json
import logging
import uuid
from datetime import datetime, timezone
from enum import Enum
from dataclasses import dataclass, asdict


class ExecutionState(str, Enum):
    PENDING = "PENDING"
    INPUT_SECURED = "INPUT_SECURED"
    PROCESSING = "PROCESSING"
    OUTPUT_SANITIZED = "OUTPUT_SANITIZED"
    COMPLETED = "COMPLETED"
    REJECTED_SECURITY_HOLD = "REJECTED_SECURITY_HOLD"


@dataclass
class AuditRecord:
    timestamp: str
    trace_id: str
    state: str
    node: str
    message: str
    user_id: str
    severity: str


class JSONAuditFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, "audit_payload"):
            return json.dumps(record.audit_payload)

        # Fallback for standard logs
        fallback = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(fallback)


class StateTransitionLogger:
    def __init__(self, log_file="audit_trail.json"):
        self.logger = logging.getLogger("AuditLogger")
        self.logger.setLevel(logging.INFO)
        # Prevent propagation to avoid duplicate logs
        self.logger.propagate = False
        self.log_file = log_file
        self._setup_handlers()

    def _setup_handlers(self):
        formatter = JSONAuditFormatter()

        # File Handler
        fh = logging.FileHandler(self.log_file)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_transition(self, trace_id, state: ExecutionState, node, msg, user_id, severity="INFO"):
        record = AuditRecord(
            timestamp=datetime.now(timezone.utc).isoformat(),
            trace_id=trace_id,
            state=state.value,
            node=node,
            message=msg,
            user_id=user_id,
            severity=severity
        )
        # Pass the payload via the 'extra' keyword argument
        self.logger.info("Audit Event", extra={"audit_payload": asdict(record)})