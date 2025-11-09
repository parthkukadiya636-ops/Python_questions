{
  "name": "My workflow 4",
  "nodes": [
    {
      "parameters": {
        "public": true,
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.3,
      "position": [
        -272,
        -80
      ],
      "id": "5d0bd5bd-c649-4e12-ac95-e6a78d376e01",
      "name": "When chat message received",
      "webhookId": "5c3dff76-10fb-43b9-9c41-81c5c51b0ffe"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 2.2,
      "position": [
        -64,
        -80
      ],
      "id": "3805920d-b9dd-47b7-81a7-e6cb648e7534",
      "name": "AI Agent"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4.1-mini"
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        -160,
        96
      ],
      "id": "aae7fee0-55e3-4a6b-856b-540799d7fac0",
      "name": "OpenAI Chat Model",
      "credentials": {
        "openAiApi": {
          "id": "VBthnS5d7fNGWrLm",
          "name": "OpenAi account"
        }
      }
    },
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.3,
      "position": [
        16,
        112
      ],
      "id": "e4a951eb-bd8c-488c-a701-f378263a42fa",
      "name": "Simple Memory"
    },
    {
      "parameters": {
        "filters": {},
        "options": {}
      },
      "type": "n8n-nodes-base.youTubeTool",
      "typeVersion": 1,
      "position": [
        208,
        96
      ],
      "id": "98ddfc17-a024-4888-9081-008435823d95",
      "name": "Get many channels in YouTube",
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "UsMOjRSdNZumAAX5",
          "name": "YouTube account"
        }
      }
    }
  ],
  "connections": {
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Get many channels in YouTube": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {},
  "triggerCount": 1,
  "meta": {
    "templateCredsSetupCompleted": true
  }
}