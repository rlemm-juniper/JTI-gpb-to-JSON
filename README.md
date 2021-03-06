![alt text](https://github.com/rlemm-juniper/JTI-gpb-to-JSON/blob/master/Google-protocol-buffer.png)![alt text](https://github.com/rlemm-juniper/JTI-gpb-to-JSON/blob/master/to.png)![alt text](https://github.com/rlemm-juniper/JTI-gpb-to-JSON/blob/master/JSON_vector_logo.svg.png)
# Summary

Created to translate JUNOS Telemetry Info from Google Protocol Buffer into JSON Format.  The python script ***convert_gpb_to_json.py*** receives GPB data on a UDP port *(default 30000)*, reformats the data into JSON for sending streaming JSON to AppFormix via REST API on a given tcp port *(8090 default)*.  Currently, this is written for Appformix, but can be modified to fit other applications.  The IP, Port and packet buffer can be changed/adjusted using optional arguments listed in the ***Usage*** section below:

## JUNOS Configuration Example:

```
services {
    analytics {
        streaming-server telemetry-server {
            remote-address 10.3.3.2;
            remote-port 30000;
        }
        export-profile appformix {
            local-address 10.255.1.2;
            local-port 21112;
            reporting-rate 60;
            format gpb;
            transport udp;
        }
        sensor cube-usage {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/services/cube/usage/;
        }                               
        sensor label-switched-path-usage {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/services/label-switched-path/usage/;
        }
        sensor mgmt-cube-usage {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/services/mgmt-cube/usage/;
        }
        sensor linecard-cpu-memory {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/system/linecard/cpu/memory/;
        }
        sensor linecard-fabric {
            server-name telemetry-server;
            export-name appformix;      
            resource /junos/system/linecard/fabric/;
        }
        sensor linecard-firewall {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/system/linecard/firewall/;
        }
        sensor linecard-interface {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/system/linecard/interface/;
            resource-filter ge-*;
        }
        sensor linecard-interface-logical-usage {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/system/linecard/interface/logical/usage/;
            resource-filter ge-*;
        }
        sensor linecard-npu-memory {
            server-name telemetry-server;
            export-name appformix;
            resource /junos/system/linecard/npu/memory/;
        }
    }
}
interfaces {
    ge-0/0/0 {
        unit 0 {
            family inet {
                address 10.3.3.1/24;
            }
        }
    }
    ge-0/0/2 {
        unit 0 {
            family inet {
                address 10.255.1.2/24;
            }
        }
    }
}
```
## Requirements for Linux Host:
```
apt-get install netcat
apt-get install protobuf-compiler
apt-get install libprotobuf-dev
```
## Required modules for Python:
```
pip install protobuf
pip install protobuf_to_dict
pip install http_client
pip install httplib
pip install http
pip install urllib
pip install requests
pip install json
pip install socket
```
## Usage:
```
usage: convert_gpb_to_json.py [-h] [-l] [-r] [-i I] [-p P] [-u U] [-b B] [-j J]
```
***Arguments (Optional):***| ***Description***
-------------------- | ----------------------------------------------
**-h, --help**           |  show this help message and exit
**-g**                   |  Log GPB Stream to Screen.  **Default is None**
**-l**                   |  Log JSON Stream to Screen.  **Default is None**
**-r**                   |  Log HTTP Requests to Screen.  **Default is None**
**-i or I**              |  Host to post JSON Stream via REST. **Default is 127.0.0.1**
**-p or P**              |  Port to post JSON Stream via REST. **Default is 8090**
**-u or U**              |  UDP Port to listen for GPB protobuf Stream. Default is **30000**
**-b or B**              |  Max Size of packet being sent by GPB protobuf. Default is 65535. **Leave it alone if you're not having problems**
**-j or J**              |  IP to listen for protobuf Stream. This is usually the local IP of the Host this script runs on. **Default is 0.0.0.0.**

## Example:

```
root@localhost# python convert_gpb_to_json.py -i 10.3.3.2 -p 8090 -u 30000 -l -r -b 65535

{"tailwind_manager": {}, "collection_name": "jdi_usage_collection", "data": {"Timestamp": 1502001079575, "jti_info": {"sensor_name": "linecard-interface-logical-usage:/junos/system/linecard/interface/logical/usage/:/junos/system/linecard/interface/logical/usage/:PFE", "version_major": 1, "timestamp": 1502001079575, "component_id": 0, "system_id": "vMX:10.255.1.2", "enterprise": {"___X": {"2636": {"___X": {"7": {"interface_info": [{"op_state": {"operational_status": "up"}, "init_time": 1501971445, "egress_stats": {"if_packets": 39087, "if_ucast_packets": 39087, "if_mcast_packets": 0, "if_octets": 17947700}, "if_name": "ge-0/0/0.0", "snmp_if_index": 520, "ingress_stats": {"if_packets": 37802, "if_ucast_packets": 37738, "if_mcast_packets": 64, "if_octets": 12219914}}, {"op_state": {"operational_status": "up"}, "init_time": 1501971445, "egress_stats": {"if_packets": 21921, "if_ucast_packets": 21921, "if_mcast_packets": 0, "if_octets": 6357870}, "if_name": "ge-0/0/2.0", "snmp_if_index": 519, "ingress_stats": {"if_packets": 26280, "if_ucast_packets": 21235, "if_mcast_packets": 5045, "if_octets": 6560331}}]}}}}}, "version_minor": 1, "sequence_number": 1771}, "roomKey": "vMX:10.255.1.2"}}
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 10.3.3.2
```
