**High-Level Package Diagram for HBnB Evolution**

## **1. Context and Objective**

In this initial phase, we are focusing on creating comprehensive technical documentation that serves as the foundation for the development of the **HBnB Evolution** application. This documentation provides an understanding of the overall architecture, the detailed design of the business logic, and the interactions within the system.

## **2. Problem Description**

The HBnB Evolution application is a simplified version of an AirBnB-like system, allowing users to perform key operations:

### **2.1 User Management**

- Users can **register, update their profiles, and be identified** as regular users or administrators.
- **Attributes**: First name, last name, email, password, admin status (boolean).
- **Operations**: Create, update, delete users.

### **2.2 Place Management**

- Users can **list properties (places) they own**, specifying details such as name, description, price, and location (latitude & longitude).
- Places are **associated with their owner**.
- Places can have a **list of amenities**.
- **Operations**: Create, update, delete, list places.

### **2.3 Review Management**

- Users can **leave reviews** for places they have visited, including a rating and a comment.
- **Operations**: Create, update, delete, list reviews by place.

### **2.4 Amenity Management**

- The system **manages amenities** that can be associated with places.
- **Attributes**: Name, description.
- **Operations**: Create, update, delete, list amenities.

### **2.5 Business Rules**

- Every object is **uniquely identified** by an ID.
- **Audit logging**: Creation and update timestamps must be recorded for all entities.

---

## **3. Three-Layer Architecture**

The application follows a **layered architecture**, consisting of:

### **3.1 Presentation Layer** (User Interaction)

- This layer includes **services and API endpoints** exposed to users.
- Responsible for handling **HTTP requests, user input, and rendering responses**.
- **Key Components:**
  - `APIController`
  - `ServiceManager`

### **3.2 Business Logic Layer** (Core Logic & Models)

- Contains the **core business logic** and models representing system entities.
- Interacts with the **Persistence Layer** to fetch and manipulate data.
- **Key Components:**
  - `User`
  - `Place`
  - `Review`
  - `Amenity`

### **3.3 Persistence Layer** (Database Access)

- Responsible for **data storage and retrieval**.
- Abstracts **database operations** via repositories or DAOs (Data Access Objects).
- **Key Components:**
  - `DatabaseManager`
  - `Repository`

---

## **4. Facade Pattern Implementation**

To simplify interactions between layers, a **Facade** acts as a unified interface:

- The **Presentation Layer** interacts only with the **Facade** instead of directly accessing the **Business Logic Layer**.
- The **Facade** calls the appropriate methods from the **Business Logic Layer**, which in turn accesses the **Persistence Layer** for data.

### **Key Components of Facade**

- `ApplicationFacade` (Acts as a bridge between Presentation and Business Logic Layer)
  - Methods for managing `User`, `Place`, `Review`, `Amenity`.
  - Calls appropriate business logic methods and returns results to the Presentation Layer.

---

## **5. Package Diagram Representation**

```mermaid
classDiagram

  %% Presentation Layer
  class APIController {
    +getUser(id)
    +getPlace(id)
    +getReview(id)
  }
  class ServiceManager {
    +fetchUser(id)
    +fetchPlace(id)
    +fetchReview(id)
  }

  %% Facade
  class ApplicationFacade {
    +getUser(id)
    +getPlace(id)
    +getReview(id)
  }

  %% Business Logic Layer
  class User {
    -id
    -firstName
    -lastName
    -email
    -password
    -isAdmin
  }
  class Place {
    -id
    -title
    -description
    -price
    -latitude
    -longitude
    -ownerId
  }
  class Review {
    -id
    -rating
    -comment
    -userId
    -placeId
  }
  class Amenity {
    -id
    -name
    -description
  }

  %% Persistence Layer
  class DatabaseManager {
    +query(sql)
    +save(object)
  }
  class Repository {
    +getUser(id)
    +getPlace(id)
    +getReview(id)
  }

  %% Relationships
  APIController --> ServiceManager
  ServiceManager --> ApplicationFacade
  ApplicationFacade --> User
  ApplicationFacade --> Place
  ApplicationFacade --> Review
  ApplicationFacade --> Amenity
  User --> Repository
  Place --> Repository
  Review --> Repository
  Amenity --> Repository
  Repository --> DatabaseManager
```

---

## **6. Explanation of Communication Pathways**

1. A user makes a request to the `APIController`.
2. The `APIController` calls `ServiceManager` to process the request.
3. The `ServiceManager` delegates the request to `ApplicationFacade`.
4. The `ApplicationFacade` retrieves relevant data by interacting with `User`, `Place`, `Review`, or `Amenity` models.
5. These models fetch data using `Repository`, which in turn interacts with `DatabaseManager` to query the database.
6. The retrieved data flows back up the chain and is returned to the user.

---

## **7. Benefits of this Architecture**

✅ **Encapsulation** – Direct access to business logic is restricted through a single Facade.\
✅ **Loose Coupling** – The Presentation Layer is not tightly coupled to business logic, making it easier to modify.\
✅ **Simplified Interaction** – Instead of handling multiple model interactions, Presentation Layer only communicates with `ApplicationFacade`.\
✅ **Scalability** – The modular design allows easy expansion of features.

---

This package diagram provides a **clear and modular architecture** for the HBnB Evolution application, ensuring **scalability and maintainability**. 🚀

