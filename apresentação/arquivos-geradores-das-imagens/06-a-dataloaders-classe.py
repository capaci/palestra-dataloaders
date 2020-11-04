class Dataloader:
    def load(key):
        """
        adiciona a chave em uma lista para executar
        a consulta posteriormente e retorna uma Promise
        """
        ...

    def batch_load_fn(key):
        """
        Recebe as chaves, faz a consulta uma vez só e retorna um resolver para a Promise
        """
        ...
