def add_course_review():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/reviews"
    body = {
        "reviewer_id": "string",
        "reviewer_name": "string",
        "mentor_id": "string",
        "thumbnail": "string",
        "review": "string",
        "rating": 1,
        "mentor_review": "string",
        "mentor_rating": 1,
        "status": "pending-review"
        }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def add_favorite_course():
    url= f"{BASE_URL}{RESOURCE_NAME}/users/{userId}/favorite-courses"
    body = {
        "course_id": "string",
        "course_name": "string"
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def add_cart_course():
    url= f"{BASE_URL}{RESOURCE_NAME}/users/{userId}/cart"
    body ={
        "course_id": "string",
        "course_name": "string",
        "price": 0,
        "discounted_price": 0
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def add_lesson_completed():
    url= f"{BASE_URL}{RESOURCE_NAME}/users/{userId}/progress-completed/{courseId}"
    body ={
        "lesson_id": "string",
        "chapter_id": "string",
        "is_completed": true,
        "lesson_duration": 0
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def approve_reject_course_review():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/reviews/approve-reject"
    body ={
        "approved_reviews": [
            {
            "PK": "string",
            "SK": "string"
            }
        ],
        "rejected_reviews": [
            {
            "PK": "string",
            "SK": "string"
            }
        ]
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def approve_reject_course():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/approve-reject"
    body ={
        "is_approved": true,
        "reason": "string",
        "add_update_items": [
            {
            "PK": "string",
            "SK": "string"
            }
        ],
        "delete_items": [
            {
            "PK": "string",
            "SK": "string"
            }
        ]
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def batch_add_cart_course():
    url= f"{BASE_URL}{RESOURCE_NAME}/users/{userId}/batch_add_cart"
    body ={
        "is_approved": true,
        "reason": "string",
        "add_update_items": [
            {
            "PK": "string",
            "SK": "string"
            }
        ],
        "delete_items": [
            {
            "PK": "string",
            "SK": "string"
            }
        ]
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def change_comment_status():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/update-comment-status"
    body ={
       #need to implement
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def course_revenue_schedule_handler():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/sales-report"
    body ={
        "report_category": "course",
        "report_type": "daily",
        "start_period": "2021 | 2021-08 | 2021-08-10",
        "end_period": "2021 | 2021-08 | 2021-08-10",
        "course_id": "string",
        "mentor_id": "string"
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())
    
def course_update_event_handler():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}"
    body ={
        "admin_status": "draft",
        "mentor_id": "string",
        "course_name": "string",
        "price": 0,
        "tags": [
            "string"
        ],
        "categories": [
            "string"
        ],
        "items_will_learn": [
            "string"
        ],
        "course_includes": [
            "string"
        ],
        "prerequisite": [
            "string"
        ],
        "course_description": "string",
        "course_description_summery": "string",
        "thumbnail": "string",
        "preview_url": "string",
        "skill_level": "beginner",
        "course_duration": 0,
        "lectures": 0,
        "requirements": "string",
        "notes": "string"
    }
    req = send_request("PUT",url,data=json.dumps(body),headers=headers )
    print(req.json())

def create_course_chapter():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/chapters"
    body ={
        "title": "string",
        "description": "string",
        "lessons": [
            {
            "name": "string",
            "url": "string",
            "resource": "string",
            "description": "string",
            "is_public": false,
            "assignment_title": "string",
            "assignment_description": "string",
            "lesson_type": "video",
            "duration": 0,
            "num_of_questions": 0
            }
        ]
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

def create_course_note():
    url= f"{BASE_URL}{RESOURCE_NAME}/courses/{courseId}/notes"
    body ={
        "title": "string",
        "description": "string",
        "is_public": true,
        "created_by_id": "string",
        "created_by_name": "string",
        "created_by_thumbnail": "string",
        "attachments": [
            "string"
        ]
    }
    req = send_request("POST",url,data=json.dumps(body),headers=headers )
    print(req.json())

