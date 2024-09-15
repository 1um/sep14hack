from typing import Any, Dict, List

from llama_index.core import StorageContext
from llama_index.core.schema import TextNode
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core.vector_stores.types import VectorStoreQuery

from actions.domain import ActionMetadata


class ActionVectorStore:
    def __init__(self):
        self.vector_store = SimpleVectorStore()
        self.storage_context = StorageContext.from_defaults(
            vector_store=self.vector_store
        )
        self.action_metadatas = {}

    def add_actions(
        self, action_metadatas: Dict[str, ActionMetadata], embed_model: Any
    ):
        nodes = []
        for action_id, action_metadata in action_metadatas.items():
            text = (
                f"{action_metadata.teaser.header} "
                f"{action_metadata.teaser.subheader} "
                f"{action_metadata.teaser.description}"
            ).strip()
            embedding = embed_model.get_text_embedding(text)
            node = TextNode(
                text=text,
                id_=action_id,
                embedding=embedding,
            )
            nodes.append(node)
            self.action_metadatas[action_id] = action_metadata

        self.vector_store.add(nodes)

    def query(self, query_embedding: List[float], top_k: int = 10):
        vector_store_query = VectorStoreQuery(
            query_embedding=query_embedding, similarity_top_k=top_k
        )
        return self.vector_store.query(vector_store_query)

    def get_action_metadata(self, action_id: str) -> ActionMetadata:
        return self.action_metadatas.get(action_id)
