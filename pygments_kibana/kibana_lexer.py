from pygments.lexer import inherit, words, bygroups
from pygments.lexers import JsonLexer
from pygments.token import Comment, Name


class KibanaLexer(JsonLexer):
    name = "Kibana Lexer"
    aliases = ["kibana"]

    flags = 0
    tokens = {
        "root": [
            (r"^#.*\n", Comment.Singleline),
            (
                words(("GET", "PUT", "POST", "HEAD", "DELETE"), suffix=r"\b"),
                Name.Builtin,
                "url",
            ),
            inherit,
        ],
        "url": [
            (
                r"([^\n\?]*)(\??)([^\n]*)",
                bygroups(Name.Entity, Name.Operator, Name.Field),
                "#pop",
            )
        ],
    }
