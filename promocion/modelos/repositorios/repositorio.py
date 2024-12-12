from modelos.repositorios.repositorio_localizacion import RepositorioLocalizacion
from modelos.repositorios.repositorio_evento import RepositorioEvento
from modelos.repositorios.repositorio_participante import RepositorioParticipante

localizacion = None
evento = None
participante = None
def obtenerRepoLocalizacion() -> 'RepositorioLocalizacion' :
    """Obtiene una única instancia del Repositoriolocalizacion."""
    global localizacion
    if localizacion == None:
        localizacion = RepositorioLocalizacion()
    return localizacion

def obtenerRepoEvento() -> 'RepositorioEvento' :
    """Obtiene una única instancia del Repositorioevento."""
    global evento
    if evento == None:
        evento = RepositorioEvento()
    return evento

def obtenerRepoParticipante() -> 'RepositorioParticipante' :
    """Obtiene una única instancia del Repositorioparticipante."""
    global participante
    if participante == None:
        participante = RepositorioParticipante()
    return participante