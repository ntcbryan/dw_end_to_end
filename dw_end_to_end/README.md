'''mermaid
flowchart TD;
    A[Início] --> Extract
    Extract --> Transform
    Transform --> Load
    Load --> E[Fim]

    subgraph Extract [Extração de Dados]
        B1[Buscar Dados de Cada Commodity]
        B2[Adicionar Dados na Lista]
        Extract --> B1 --> B2
    end

    subgraph Transform [Transformação de Dados]
        C1[Concatenar Todos os Dados]
        C2[Preparar DataFrame com Pandas]
        Transform --> C1 --> C2
    end

    subgraph Load [Carga no PostgreSQL]
        D1[Salvar DataFrame com SQLAlchemy]
        Load --> D1
    end
'''