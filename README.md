# Unciv Server Email Notifyer

Hosts a server for Unciv. Contains a service which will keep track of player IDs and associates an email with each one. Every set interval, for each game stored on the server, the service checks if a new turn has been taken and then sends out an email notification to the player whose turn it is, if the player ID has an email associated with it.
