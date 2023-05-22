{
    "version": 2,
    "builds": [
      {
        "src": "dl_models/wsgi.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "dl_models/wsgi.py"
      }
    ]
}