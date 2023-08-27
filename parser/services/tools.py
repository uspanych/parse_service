import abc


class AbstractParser(abc.ABC):
    @abc.abstractmethod
    async def search_data(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError
