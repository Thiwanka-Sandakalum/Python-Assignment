from services.interfaces import IElasticService

class ElasticService(IElasticService):
    def __init__(self, client, index_name):
        self.client = client
        self.index_name = index_name
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self):
        if not self.client.indices.exists(index=self.index_name):
            mapping = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                },
                "mappings": {
                    "properties": {
                        "application_name": {"type": "keyword"},
                        "service_name": {"type": "keyword"},
                        "service_status": {"type": "keyword"},
                        "host_name": {"type": "keyword"},
                        "timestamp": {"type": "date"}
                    }
                }
            }
            self.client.indices.create(
                index=self.index_name,
                body=mapping
            )

    def index_document(self, payload: dict):
        return self.client.index(
            index=self.index_name,
            document=payload
        )

    def get_latest_service(self, service_name: str):
        query = {
            "query": {
                "term": {"service_name.keyword": service_name}
            },
            "sort": [{"timestamp": {"order": "desc"}}],
            "size": 1
        }
        response = self.client.search(
            index=self.index_name,
            body=query
        )
        hits = response.get("hits", {}).get("hits", [])
        return hits[0]["_source"] if hits else None

    def get_all_latest(self):
        query = {
            "sort": [{"timestamp": {"order": "desc"}}],
            "size": 100
        }
        response = self.client.search(
            index=self.index_name,
            body=query
        )
        return [hit["_source"] for hit in response["hits"]["hits"]]
