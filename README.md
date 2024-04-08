# Credit-Risk-Modelling

# Idee per il modello

-Per come io immagino il sistema, vedo come i parametri di input parametri che definiscano in ogni momento una probabilità p di fallimento dell utente. Tutto sta a capire quando è questa probabilità p. In finanza si stima il richio associato al fallimento con una probabilità p e i cashflow futuri che devono rientrare. L idea è fare esattamente questo. Il modello deve solo capire cosa è p.

- Il concetto è di survivorship. Dove però dobbaimo essere in grado di stimare quanto ogni singolo attributo causa un default di sistema
- Se vediamo troppi dati buttiamo tutto in un modello deep e via e vediamo che esce fuori da bravi data scientist ovviamente 
# idee che scarterei

- Time series. Il modello non ha conoscenza di cosa è prima o dopo, non deve imparare una logica pregressa che si ripete
