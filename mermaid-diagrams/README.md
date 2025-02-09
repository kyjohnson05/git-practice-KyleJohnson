# Pokemon Card Storage Web App
## 1. Entity-Relationship Diagram (ERD)
```mermaid
erDiagram
USER ||--o{ DECK : owns
USER ||--o{ CARD : submits
USER {
string name
}
ADMIN ||--|{ CARD : manages
ADMIN {
string name
}
DECK }|--|{ CARD : contains
CARD {
string pokemon_name
string type
string rarity
string move
int damage
int defense
int level
}
DECK {
string owner_name
int card_quantity
}
```
---
## 2. User Flow Diagram
```mermaid
flowchart TD
A[Start] --> B{Log in as User or Admin?}
B -->|User| C[View all Pokemon Cards]
B -->|Admin| D[Manage Cards]
C --> E[Create Deck]
C --> F[Submit New Card]
D --> I{Approve or Deny Card?}
D --> M[Modify/Delete Card]
D --> N[Add New Card]
E --> G[Edit Deck]
F --> H[Admin Approval Requested]
G --> J[Add/Remove Card]
H --> I -->|Approve| K[Visible Card]
H --> I -->|Deny| P[Hidden Card]
J --> O[Submit Deck]
K --> L[Card Database]
M --> L
N --> L
O --> Q[End]
```
---
## 3. System Architecture Diagram
```mermaid
graph TD
A[User] -->|HTTP Request| B[Frontend UI]
B -->|API Request| C[Backend API]
C -->|Data Query/Update| D[(Database)]
D --> C
C --> B
B --> A
E[Admin] -->|HTTP Request| F[Admin Dashboard]
F -->|API Request| C
subgraph Access Control
C --- G[User Deck Management]
C --- H[Admin Card Management]
end
```
---
## 4. API Endpoints Table
```mermaid
classDiagram
class "API Endpoints" {
GET /api/cards : Fetch all cards
POST /api/cards : Submit new card (User)
PUT /api/cards/:id : Modify card (Admin)
DELETE /api/cards/:id : Delete card (Admin)
GET /api/user/decks : Fetch all decks (User)
POST /api/user/decks : Create new deck (User)
PUT /api/decks/:id : Manage deck (User)
DELETE /api/decks/:id : Delete deck (User)
GET /api/admin/cards : Fetch pending cards (Admin)
PUT /api/admin/cards/:id/approve : Approve card (Admin)
}
```
