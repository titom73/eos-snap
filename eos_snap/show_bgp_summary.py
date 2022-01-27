from email import header


#!/usr/bin/python
# coding: utf-8 -*-

EOS_DATA = """
{
    "jsonrpc": "2.0",
    "id": "EapiExplorer-1",
    "result": [
        {},
        {
            "vrfs": {
                "default": {
                    "routerId": "192.168.0.2",
                    "peers": {
                        "192.168.255.8": {
                            "description": "EAPI-LEAF4A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.67221,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65104"
                        },
                        "192.168.255.9": {
                            "description": "EAPI-BL01A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.671742,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65105"
                        },
                        "192.168.255.3": {
                            "description": "EAPI-LEAF1A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.684075,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65101"
                        },
                        "192.168.255.4": {
                            "description": "EAPI-LEAF1B",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.672388,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65101"
                        },
                        "192.168.255.5": {
                            "description": "EAPI-LEAF2A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.671318,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65102"
                        },
                        "192.168.255.6": {
                            "description": "EAPI-LEAF2B",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.684447,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65102"
                        },
                        "192.168.255.7": {
                            "description": "EAPI-LEAF3A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.67202,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65103"
                        },
                        "192.168.255.12": {
                            "description": "EAPI-CL01B",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.671542,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65106"
                        },
                        "192.168.255.10": {
                            "description": "EAPI-BL01B",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.672576,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65105"
                        },
                        "192.168.255.11": {
                            "description": "EAPI-CL01A",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.684262,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65106"
                        },
                        "192.168.253.2": {
                            "description": "EAPI-L2LEAF01",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.651551,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65107"
                        },
                        "192.168.253.3": {
                            "description": "EAPI-L2LEAF02",
                            "msgSent": 0,
                            "inMsgQueue": 0,
                            "prefixReceived": 0,
                            "upDownTime": 1643205722.672777,
                            "version": 4,
                            "prefixAccepted": 0,
                            "msgReceived": 0,
                            "peerState": "Active",
                            "outMsgQueue": 0,
                            "underMaintenance": "false",
                            "asn": "65108"
                        }
                    },
                    "vrf": "default",
                    "asn": "65000"
                }
            }
        }
    ]
}
"""
