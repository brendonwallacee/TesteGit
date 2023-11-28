from abc import ABC, abstractmethod
from typing import List

from beans.MedicamentoBean import MedicamentoBean


class MedicamentoDAOListener(ABC):
    @abstractmethod
    def atualizar(self, remedio: MedicamentoBean) -> None:
        pass

    @abstractmethod
    def excluir(self, remedio: MedicamentoBean) -> None:
        pass

    @abstractmethod
    def procurarMedicamento(self, nome: str) -> MedicamentoBean:
        pass

    @abstractmethod
    def salvar(self, remedio: MedicamentoBean) -> None:
        pass

    def alarmar(self, remedio: MedicamentoBean, hora) -> None:
        pass

    @abstractmethod
    def todosMedicamentos(self) -> List:
        pass
