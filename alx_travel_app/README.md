# ALX Travel App — Milestone 2

This project implements database models, serializers, and a custom seeder command for populating the database with sample data.

## Features

- Django models for:
  - Listing
  - Booking
  - Review
- DRF serializers for:
  - Listing
  - Booking
- Custom management command:
  - `seed` — populates the database with sample listings.

## Running the Seeder

Run the command below:
python manage.py seed


This will create sample listings for development and testing.

## Directory Structure

alx_travel_app/
├── listings/
│   ├── models.py
│   ├── serializers.py
│   ├── management/commands/seed.py


## API Endpoints for Listings and Bookings

This project implements Django REST Framework (DRF) API endpoints for managing
travel listings and bookings.

### Steps Completed

1. Project duplicated from `alx_travel_app_0x00` → `alx_travel_app_0x01`
2. Implemented ModelViewSets:
   - `ListingViewSet`
   - `BookingViewSet`
3. Configured DRF router under `/api/`
4. Endpoints tested with Postman (CRUD operations)

### API Routes

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| GET    | /api/listings/        | List all listings         |
| POST   | /api/listings/        | Create a new listing      |
| GET    | /api/listings/<id>/   | Retrieve a listing        |
| PUT    | /api/listings/<id>/   | Update a listing          |
| DELETE | /api/listings/<id>/   | Delete a listing          |
| GET    | /api/bookings/        | List all bookings         |
| POST   | /api/bookings/        | Create a new booking      |
| GET    | /api/bookings/<id>/   | Retrieve a booking        |
| PUT    | /api/bookings/<id>/   | Update a booking          |
| DELETE | /api/bookings/<id>/   | Delete a booking          |

### Testing

All endpoints were tested using Postman with the following operations:
- GET
- POST
- PUT
- DELETE


