===========================
Different kinds of diagrams
===========================

PlantUML
========

.. uml::

    Alice -> Bob: Hi!
    Alice <- Bob: How are you?

Mermaid
=======

.. mermaid::

    flowchart LR

      subgraph sensors

         subgraph ism
            RF-1[RF sensor 1]
            RF-2[RF sensor 2]
            RF-N[RF sensor N]
            relay{{telemetry relay}}
         end
         subgraph sub1ghz
            LORAWAN[LoRaWAN sensor]
            LORA[LoRa sensor]
         end
         subgraph cellular
            CELL-GSM[GSM sensor]
            CELL-LTE[LTE M1/NB1 sensor]
         end

         gateway{{network gateway}}

         RF-1  --> relay
         RF-2  --> relay
         RF-N  --> relay
         relay --> gateway

         TTN{TTN}

      end

      %% Breadboard

      %% Sensors
      LORAWAN     --> TTN
      LORA        --> gateway

      %% Network
      gateway     --> network
      TTN         --> network

      CELL-GSM  --> network
      CELL-LTE  --> network
