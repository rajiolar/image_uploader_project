from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
from dotenv import load_dotenv
from schema import user as  userSchema
from model.user import User
from dependencies.db import get_db
from services import user as userService
import os
import json


# Load environment variables
load_dotenv()
cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
api_key = os.getenv("CLOUDINARY_API_KEY")
api_secret = os.getenv("CLOUDINARY_API_SECRET")

# Configure Cloudinary
cloudinary.config(
    cloud_name=cloud_name, api_key=api_key, api_secret=api_secret, secure=True
)

app = FastAPI()

# # Upload image endpoint
# @app.post("/upload/image")
# async def image_uploader(file: UploadFile):
#     try:
#         # Read the file content asynchronously
#         file_content = await file.read()

#         newFileName = file.filename.split(".")[0].replace(" ", "")

#         # Upload file to Cloudinary
#         cloudinary.uploader.upload(file_content, public_id=newFileName)

#         # Build the URL of the uploaded image
#         url = CloudinaryImage(public_id=newFileName).build_url()

#         # Increment and track image count in file
#         FILENAME = "IdTracker.txt"
#         IMAGEFILE = "imageDB.json"

#         # Read current count from file
#         with open(FILENAME, "r") as tracker_file:
#             count = int(tracker_file.read())

#         # Increment count
#         count += 1

#         # write it back to the file
#         with open(FILENAME, "w") as tracker_file:
#             tracker_file.write(str(count))

#         # reading the existing JSON data
#         with open(IMAGEFILE, "r") as json_file:
#             loaded_JSON = json.load(json_file)

#         # updating the JSON data
#         loaded_JSON[count] = url

#         # writing the updated JSON data directly to the file
#         with open(IMAGEFILE, "w") as json_file:
#             json.dump(loaded_JSON, json_file, indent=4)

#         # Return success message and image URL
#         return {
#             "message": "Image uploaded successfully",
#             "url": url,
#             "Image ID": count,
#             "Filename": file.filename,
#         }

#     except Exception as e:
#         # Handle any exceptions and return an error message
#         raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")


# @app.get("/download/image/{image_id}")
# async def retrieve_image(image_id:str):
#         with open("imageDB.json") as json_file:
#             json_data = json.load(json_file)

#         if str(image_id) in json_data:
#             return {
#                 "message": "Image retrieved successfully",
#                 "url": json_data[str(image_id)],
#                 "Image ID": image_id,
#             }
#         else:
#             raise HTTPException(status_code=404, detail="Image ID not found")

@app.post("/usr/signup", response_model= userSchema.SignupResponse)
async def create_user( user : userSchema.UserCreate, db : Session = Depends(get_db)):
    data = userService.create_user(user, db)
    
    return data

