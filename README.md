
Subjects list:

    curl -s -X GET http://localhost:8000/api/v1/subjects/ | jq
    [
    {
        "id": 6,
        "title": "Administration",
        "slug": "administration"
    },
    {
        "id": 5,
        "title": "Programming",
        "slug": "programming"
    }
    ]

Subject with id = 5:

    curl -s -X GET http://localhost:8000/api/v1/subjects/5 | jq
    {
    "id": 5,
    "title": "Programming",
    "slug": "programming"
    }

Courses list:

    curl -s -X GET http://localhost:8000/api/v1/courses/ | jq
    [
    {
        "id": 4,
        "subject": 6,
        "title": "Linux",
        "slug": "linux",
        "overview": "Linux",
        "created": "2019-06-09T19:07:52.804628Z",
        "owner": 1,
        "modules": [
        {
            "id": 11,
            "title": "Architecture",
            "description": "stuff"
        },
        {
            "id": 12,
            "title": "Security",
            "description": "Security and monitoring"
        },
        {
            "id": 13,
            "title": "Networking",
            "description": "dns, dhcp, vlan, lacp, vrrp, iptables"
        }
        ]
    },
    {
        "id": 3,
        "subject": 6,
        "title": "DevOps",
        "slug": "devops",
        "overview": "DevOps",
        "created": "2019-06-09T18:48:06.521739Z",
        "owner": 1,
        "modules": [
        {
            "id": 7,
            "title": "Module 1",
            "description": "GCP\r\nGit"
        },
        {
            "id": 8,
            "title": "Module 2",
            "description": "Ansible"
        },
        {
            "id": 9,
            "title": "Module 3",
            "description": "Docker"
        },
        {
            "id": 10,
            "title": "Module 4",
            "description": "Prometheus"
        }
        ]
    },
    {
        "id": 2,
        "subject": 5,
        "title": "Python",
        "slug": "python",
        "overview": "Python",
        "created": "2019-06-09T18:45:31.089925Z",
        "owner": 1,
        "modules": [
        {
            "id": 4,
            "title": "Basics",
            "description": "OOP\r\nTesting"
        },
        {
            "id": 5,
            "title": "Web",
            "description": "Django\r\nREST"
        },
        {
            "id": 6,
            "title": "Data Engineering",
            "description": "NumPy\r\nPandas"
        }
        ]
    },
    {
        "id": 1,
        "subject": 5,
        "title": "Web-python",
        "slug": "web-python",
        "overview": "django, flask, js, bootstrap",
        "created": "2019-06-09T18:36:47.556590Z",
        "owner": 1,
        "modules": [
        {
            "id": 1,
            "title": "Module 1",
            "description": "Backend"
        },
        {
            "id": 2,
            "title": "Module 2",
            "description": "Frontend"
        },
        {
            "id": 3,
            "title": "Module 3",
            "description": "CI/CD"
        }
        ]
    }
    ]

Course with id = 2:

    curl -s -X GET http://localhost:8000/api/v1/courses/2/ | jq
    {
    "id": 2,
    "subject": 5,
    "title": "Python",
    "slug": "python",
    "overview": "Python",
    "created": "2019-06-09T18:45:31.089925Z",
    "owner": 1,
    "modules": [
        {
        "id": 4,
        "title": "Basics",
        "description": "OOP\r\nTesting"
        },
        {
        "id": 5,
        "title": "Web",
        "description": "Django\r\nREST"
        },
        {
        "id": 6,
        "title": "Data Engineering",
        "description": "NumPy\r\nPandas"
        }
    ]
    }

Lets enroll in course with id = 2:

    curl -s -X GET http://localhost:8000/api/v1/courses/2/enroll/ | jq
    Unauthorized: /api/v1/courses/2/enroll/
    {
    "detail": "Authentication credentials were not provided."
    }

    curl -s -u user1:password1 -X GET http://localhost:8000/api/v1/courses/2/enroll/ | jq
    Method Not Allowed: /api/v1/courses/2/enroll/
    {
    "detail": "Method \"GET\" not allowed."
    }

    curl -s -u user1:password1 -X POST http://localhost:8000/api/v1/courses/2/enroll/ | jq
    {
    "enrolled": true
    }

User registation:

    curl -s -X POST http://localhost:8000/api/v1/users/ | jq
    Bad Request: /api/v1/users/
    {
    "username": [
        "This field is required."
    ],
    "password": [
        "This field is required."
    ]
    }

    curl -s  -d '{"username":"user3", "password":"password3"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/users/ | jq
    {
    "id": 4,
    "username": "user3"
    }
