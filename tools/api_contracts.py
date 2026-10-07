"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = None

ENDPOINTS = {
    "serp_google": {
        "method": "POST",
        "path": "/serp/google",
        "operation": "search",
        "schema": {
            "type": "object",
            "required": ["query"],
            "properties": {
                "page": {"type": "integer", "minimum": 1, "maximum": 100},
                "type": {
                    "enum": ["search", "images", "news", "maps", "places", "videos"],
                    "type": "string",
                },
                "query": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 2048,
                    "pattern": ".*\\S.*",
                },
                "range": {
                    "type": "string",
                    "enum": ["h", "d", "w", "m", "y", "qdr:h", "qdr:d", "qdr:w", "qdr:m", "qdr:y"],
                },
                "number": {"type": "integer", "minimum": 1, "maximum": 100},
                "country": {"type": "string", "minLength": 1, "maxLength": 32},
                "language": {"type": "string", "minLength": 1, "maxLength": 32},
                "image_size": {
                    "type": "string",
                    "enum": [
                        "large",
                        "medium",
                        "icon",
                        "2mp",
                        "4mp",
                        "6mp",
                        "8mp",
                        "10mp",
                        "12mp",
                        "15mp",
                        "20mp",
                        "40mp",
                        "70mp",
                    ],
                },
            },
            "additionalProperties": False,
            "oneOf": [
                {
                    "properties": {"type": {"type": "string", "enum": ["images"]}},
                    "required": ["type"],
                },
                {
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["search", "news", "maps", "places", "videos"],
                        }
                    },
                    "not": {"required": ["image_size"]},
                },
            ],
        },
        "properties": {
            "page": {"type": "integer", "minimum": 1, "maximum": 100},
            "type": {
                "enum": ["search", "images", "news", "maps", "places", "videos"],
                "type": "string",
            },
            "query": {"type": "string", "minLength": 1, "maxLength": 2048, "pattern": ".*\\S.*"},
            "range": {
                "type": "string",
                "enum": ["h", "d", "w", "m", "y", "qdr:h", "qdr:d", "qdr:w", "qdr:m", "qdr:y"],
            },
            "number": {"type": "integer", "minimum": 1, "maximum": 100},
            "country": {"type": "string", "minLength": 1, "maxLength": 32},
            "language": {"type": "string", "minLength": 1, "maxLength": 32},
            "image_size": {
                "type": "string",
                "enum": [
                    "large",
                    "medium",
                    "icon",
                    "2mp",
                    "4mp",
                    "6mp",
                    "8mp",
                    "10mp",
                    "12mp",
                    "15mp",
                    "20mp",
                    "40mp",
                    "70mp",
                ],
            },
        },
        "parameters": [],
        "defaults": {"type": "search", "number": 3, "page": 1},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    }
}
