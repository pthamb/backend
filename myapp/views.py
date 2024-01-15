import time
from django.shortcuts import render
from .models import UserProfile
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import logging
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from social_django.models import UserSocialAuth
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.permissions import AllowAny
from django.core.files.storage import FileSystemStorage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import json
import math
import requests
import os
logger = logging.getLogger(__name__)


# Get an instance of a logger



@csrf_exempt
def user_profile_to_dict(user_profile):
    return {
        "id": user_profile.id,
        "name": user_profile.name,
        "age": user_profile.age,
        "email": user_profile.user.email,
        "zipCode": user_profile.zipCode,
        "countryCode": user_profile.countryCode,
        "mobile": user_profile.mobile,
        "picture":user_profile.picture,
        "walking":user_profile.walking,
        "running":user_profile.running,
        "dog": user_profile.dog,
        "gardening":user_profile.gardening,
        "swimming":user_profile.swimming,
        "coffeeTea":user_profile.coffeeTea,
        "art": user_profile.art,
        "foodGathering":user_profile.foodGathering,
        # "televisionSports":user_profile.televisionSports,
        "sports": user_profile.sports,
        "movies":user_profile.movies,
        "shopping":user_profile.shopping,
        "happyHours":user_profile.happyHours,
        # "errands":user_profile.errands,
        "rides":user_profile.rides,
        "childcare":user_profile.childcare,
        "eldercare":user_profile.eldercare,
        "petcare":user_profile.petcare,
        "tutoring":user_profile.tutoring,
        "repairAdvice":user_profile.repairAdvice,
        # "otherAdvice":user_profile.otherAdvice,
        "latitude":user_profile.latitude,
        "longitude":user_profile.longitude,
        # "sharePreference":user_profile.sharePreference,
        "email_confirmed":user_profile.email_confirmed,
        "interests_updated": user_profile.interests_updated,
        "confirmation_token": str(user_profile.confirmation_token)
        # Add other fields as necessary
    }



@csrf_exempt
@require_POST 
def register(request):
    if request.method == 'POST':
        
        # uploaded_file_url = None
        try:
            # data = json.loads(request.body)
            # print(f"data:{data}")
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            zipCode = request.POST.get('zipCode')
            countryCode = request.POST.get('countryCode')
            password = request.POST.get('password')
            picture = request.FILES.get('picture')  # Access uploaded file
            print(f"name: {name}, email: {email}, picture: {picture}")
            # if picture:
            #   try:
            #     img = Image.open(picture)
            #     img.thumbnail((800, 800))  # example size, adjust as needed

            #     # Save the resized image to a BytesIO object
            #     in_memory_file = BytesIO()
            #     img.save(in_memory_file, format=img.format)
            #     in_memory_file.seek(0)

            #     # Generate a new filename
            #     filename = f"{user.id}_{int(time.time())}.{img.format.lower()}"
            #     picture = ContentFile(in_memory_file.read(), name=filename)
            #     fs = FileSystemStorage()
            #     filename = fs.save(picture.name, picture)
            #     uploaded_file_url = request.build_absolute_uri(fs.url(filename))
            #   except Exception as e:
            #     # Handle exceptions
            #     print(f"Error handling image: {e}")
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format or empty request body'}, status=400)


        required_fields = ["name", "age", "email", "mobile", "zipCode"]
        missing_fields = [field for field in required_fields if not request.POST.get(field)]
        if missing_fields:
            messages.error(request, "Please fill out the required fields: " + ', '.join(missing_fields))
            return JsonResponse({'message': 'Fill all the required field'},status=400)

       
        
        print(f"email:{email}")
        if User.objects.filter(username=email).exists():
        #    return JsonResponse({'error': 'User with this email already exists.'}, status=400)
            return JsonResponse({'error': f'User with the email {email} already exists.'}, status=400)
        
        
        # print(f"email:{email}")
        # Assuming validation passes, create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        
        uploaded_file_url = None
        if picture:
              try:
                img = Image.open(picture)
                img.thumbnail((800, 800))  # example size, adjust as needed

                # Save the resized image to a BytesIO object
                in_memory_file = BytesIO()
                img.save(in_memory_file, format=img.format)
                in_memory_file.seek(0)

                # Generate a new filename
                filename = f"{user.id}_{int(time.time())}.{img.format.lower()}"
                picture = ContentFile(in_memory_file.read(), name=filename)
                fs = FileSystemStorage()
                filename = fs.save(picture.name, picture)
                uploaded_file_url = request.build_absolute_uri(fs.url(filename))
              except Exception as e:
                # Handle exceptions
                print(f"Error handling image: {e}")
        # picture=data.get('picture')
        # print(f"picture:{picture}")
        
        

        # Create UserProfile with array data stored as strings
        # user_profile = UserProfile(
        #     user=user,
        #     name=data.get('name'),
        #     age=data.get('age'),
        #     email=data.get('email'),
        #     zipCode=data.get('zipCode'),
        #     countryCode=data.get('countryCode'),
        #     mobile=data.get('mobile'),
        #     picture=data.get('picture'),
        #     # latitude = data.get('latitude'),
        #     # longitude = data.get('longitude'),
        #     email_confirmed=False
        # )
        
        user_profile = UserProfile(
            user=user,
            name=name,
            age=age,
            email=email,
            zipCode=zipCode,
            countryCode=countryCode,
            mobile=mobile,
            picture=uploaded_file_url,
            email_confirmed=False
        )
        # print(f"user:{user_profile}")
        user_profile.save()
        user_profile_data = user_profile_to_dict(user_profile)
        
        print(f"user:{user_profile_data}")
        
        # if missing_fields:
        #     messages.error(request, "Please fill out the required fields: " + ', '.join(missing_fields))
        #     return JsonResponse({'message': 'Fill all the required field'},status=400)
        
        messages.success(request, "Data submitted successfully!")
        
        # Generate confirmation URL
        # confirm_url = request.build_absolute_uri('/confirm_email/') + str(user_profile.confirmation_token)
        confirm_url = f'http://localhost:5173/verification/{user_profile.confirmation_token}'


        # Send email
        send_mail(
            'Confirm your email',
            f'Please click the following link to confirm your email: {confirm_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )


        # Return a success response
        return JsonResponse({'message': 'Verfication email sent','token': token.key}, status=201)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
@require_http_methods(["GET","POST"])
def confirm_email(request, token):
    try:
        user_profile = UserProfile.objects.get(confirmation_token=token)
        user_profile.email_confirmed = True
        user_profile.save()
        # Instead of using Django's messages and redirect, return a JSON response
        return JsonResponse({'message': "Email Verified!"}, status=200)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': "Invalid confirmation link!"}, status=400)
    
    
    

# @csrf_exempt
# @require_POST
# def resend_confirmation(request):
#     try:
#         data = json.loads(request.body)
#         email = data.get('email')

#         # Find user and profile
#         user = User.objects.get(email=email)
#         user_profile = UserProfile.objects.get(user=user)

#         # Resend the email
#         confirm_url = f'http://your-react-app.com/verification/{user_profile.confirmation_token}'
#         send_mail(
#             'Confirm your email',
#             f'Please click the following link to confirm your email: {confirm_url}',
#             settings.DEFAULT_FROM_EMAIL,
#             [user.email],
#             fail_silently=False,
#         )

#         return JsonResponse({'message': 'Confirmation email resent successfully!'}, status=200)
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User does not exist'}, status=404)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
    
    
    
    
# @csrf_exempt
# def facebook_login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data['name']
#         email = data['email']
#         picture = data['picture']['data']['url']
#         # token = data['accessToken']

#         # Check if the user already exists
#         user, created = User.objects.get_or_create(username=email, defaults={'email': email})
#         if created:
#             # Create a profile for the new user
#            UserProfile.objects.create(user=user, name=name, email=email, picture=picture)
           
           
#         return JsonResponse({'status': 'Success', 'message': 'Logged in with Facebook'})
#     else:
#         return JsonResponse({'status': 'Error', 'message': 'Invalid request'}, status=400)    
    
    
    


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def google_login(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('name')
        picture = data.get('picture')

        print(f"data:{data}")
        # Check if the user already exists
        user, created = User.objects.get_or_create(username=email, defaults={'email': email})
        
        if created:
            # If the user is new, create a user profile
            user_profile = UserProfile.objects.create(user=user, name=name, email=email, picture=picture)
            token, _ = Token.objects.get_or_create(user=user)
            user_profile_data = user_profile_to_dict(user_profile)
            response_data = {
                'status': 'Success',
                'message': 'Logged in with Google',
                'token': token.key,
                'user' : user_profile_data
            }
        else:
            # If the user already exists, just retrieve the token
            # token, _ = Token.objects.get_or_create(user=user)
            user_profile, created = UserProfile.objects.get_or_create(user=user)  # Retrieve the user profile
            token, _ = Token.objects.get_or_create(user=user)
            user_profile_data = user_profile_to_dict(user_profile)  # Convert user profile to dict
            response_data = {
                'status': 'Success',
                'message': 'User already exists. Logged in successfully',
                'token': token.key,
                'user': user_profile_data
                
            }

        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'status': 'Error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    


@csrf_exempt
def user_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are accepted'}, status=405)
 
    try:
    
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(f"Received email: {email}, password: {password}")

        if not email or not password:
                return JsonResponse({'error': 'Email and password are required fields.'}, status=400)
        
        user = authenticate(request, username=email, password=password)

        print(f"user:{user}")
        print("today")

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            # print(f"token:{token}")
            try:
                user_profile = UserProfile.objects.get(user=user)
                user_profile_data = user_profile_to_dict(user_profile)
                print(f"token:{token}")
                
            except UserProfile.DoesNotExist:
                user_profile_data = {}
            return JsonResponse({'message': 'Login successful', 'token': token.key, 'user': user_profile_data})
        else:
           
            return JsonResponse({'error': 'Invalid login credentials'}, status=401)
   
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'An error occurred during login'}, status=500)
    
    

    
@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted_page(request):
    
    for header, value in request.headers.items():
        # print(f"{header}: {value}")
     try:
        # Get the user from the request
        user = request.user
        
        # Retrieve the user profile
        user_profile = UserProfile.objects.get(user=user)
        user_profile_data = user_profile_to_dict(user_profile)

        return Response({
            'message': 'Access granted',
            'user': user_profile_data
        })
        
        

     except UserProfile.DoesNotExist:
        return Response({'message': 'Request unauthorized, please login'}, status=404)
     except Exception as e:
        return Response({'message': f'An error occurred: {str(e)}'}, status=500)
    
    
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_interests(request):
    try:
        user = request.user
        data = json.loads(request.body)
        
        print(f"data:{data}")
        user_profile = UserProfile.objects.get(user=user)
        
        # Initially, set interests_updated to False
        interests_updated = False
        walking= data.get('walking')
        # Define all your interest fields and their corresponding optionsKey
        interest_fields = {
            'walking': 'walkingSpeed', 
            'running': 'runningType', 
            'dog': 'dogWalks', 
            'gardening': None, 
            'swimming': 'swimmingPlace',
            'coffeeTea': 'coffeeTeaPlace',
            'art': 'artType',
            'foodGathering': 'foodGatheringType',
            'sports': 'sportsType',
            'movies': 'movieType',
            'shopping': 'shoppingType',
            'happyHours': 'happyHoursType',
            'rides': 'ridesType',
            'childcare': 'childcareType',
            'eldercare': 'eldercareType',
            'petcare': 'petcareType',
            'repairAdvice': 'repairAdviceType',
            'tutoring': 'tutoringType'
            # 'errands': 'errandsType'
        }
        
        print(f"walking:{walking}")

        # Loop through each interest field and handle the expected structure
        for field, optionsKey in interest_fields.items():
            # print(f"interest_field:{interest_fields.items()}")
            if field in data:
                # Extract the boolean value indicating interest from questionKey
                interested = data[field]  # this is assumed to be a boolean from your frontend
                print(f"intrested:{interested}")

                # Initialize details as None, it will be updated if optionsKey is not None and exists in data
                details = None

                # If there's an optionsKey and it exists in the data, extract the details
                if optionsKey and optionsKey in data:
                    details = data[optionsKey]

                # Format the data as expected and save it to the user profile
                interest_data = {
                    'interested': interested,
                    'details': details
                }
                setattr(user_profile, field, interest_data)
                print(f"intersted_data:{interest_data}")
                # print(f"user_profile:{user_profile}")
                interests_updated = True
                latitude = data.get('latitude')
                longitude = data.get('longitude')
                
        # Update the user profile with interests_updated flag
        if interests_updated:
            user_profile.interests_updated = interests_updated
            user_profile.latitude = latitude
            user_profile.longitude = longitude
            user_profile.save()
            # print(f"user_profile:{user_profile}")

        # Convert user profile to a dictionary or appropriate format before sending it in response
        user_profile_data = user_profile_to_dict(user_profile)  # Ensure this function exists and converts the profile to a suitable format
        token, _ = Token.objects.get_or_create(user=user)
        print(f"user_profile:{user_profile_data}")
        
        return JsonResponse({
            'message': 'Interests updated successfully',
            'user_profile': user_profile_data,
            'token': token.key,
            'interests_updated': interests_updated
        })

    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User profile not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

    
    


def user_logout(request):
    logout(request)





def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km

    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance





def calculate_similarity(user1, user2):
    fields = ['walking', 'running', 'dog', 'gardening', 'swimming', 'coffeeTea', 'art', 'foodGathering', 'sports', 'movies', 'shopping', 'happyHours', 'rides', 'childcare', 'eldercare', 'petcare', 'tutoring', 'repairAdvice']
    matches = 0
    valid_fields = 0
    matching_fields = []

    for field in fields:
        user1_field = getattr(user1, field, {})
        user2_field = getattr(user2, field, {})

        user1_interested = user1_field.get('interested', False)
        user2_interested = user2_field.get('interested', False)

        # Consider field for comparison only if both users are interested
        if user1_interested and user2_interested:
            valid_fields += 1

            user1_details = user1_field.get('details')
            user2_details = user2_field.get('details')

            # Count as a match if details are the same
            # if user1_details == user2_details:
            #     matches += 1
            #     matching_fields.append(field)
            # if user1_details == user2_details or (user1_details is None and user2_details is None):
            #     matches += 1
            #     matching_fields.append(field)
            
            if user1_interested and user2_interested:
                    matches += 1
                    matching_fields.append(field)
                # Also, count as a match if details are the same (including both being None)
            elif user1_details == user2_details:
                    matches += 1
                    matching_fields.append(field)

    # Avoid division by zero if no valid fields for comparison
    if valid_fields == 0:
        return 0, []

    similarity = (matches / valid_fields) * 100
    return similarity, matching_fields





@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_similar_users(request):
    try:
        # data = request.data
        current_user = request.user
        current_user_profile = UserProfile.objects.get(user=current_user)
        print(f"current:{current_user}")

        # Check if the current user is within a 5km radius and has a 50% data match
        similar_users = []
        for user in UserProfile.objects.exclude(user=current_user):
            distance = haversine(current_user_profile.latitude, current_user_profile.longitude, user.latitude, user.longitude)
            # if distance <= 5 and calculate_similarity(current_user_profile, user) >= 50:
            #     similar_users.append(user_profile_to_dict(user))
            print(f"user:{user}")
            print(f"Checking user: {user}, Distance: {distance} km")
            print(f"current_user_profile:{current_user_profile}")
            # if distance <= 5:
        
            similarity, matching_fields = calculate_similarity(current_user_profile, user)
            print(f"user:{user}")
            print(f"Distance: {distance}, Similarity: {similarity}%, User: {user}, Matching Fields: {matching_fields}")
            # if calculate_similarity(current_user_profile, user):
            if distance <= 5 and similarity> 50:
                    similar_users.append(user_profile_to_dict(user))
                    

        if similar_users:
            return Response({'users': similar_users})
        else:
            return Response({'message': 'No similar users found'}, status=404)

    except UserProfile.DoesNotExist:
        return Response({'message': 'Current user profile not found'}, status=404)
    except Exception as e:
        return Response({'message': f'An error occurred: {str(e)}'}, status=500)
    




@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_similar_user_profile(request):   # type: ignore
    try:
        logger.info(f"Received query parameters: {request.GET}")

        # Fetching the 'id' parameter from the query string
        user_id = request.GET.get('id', None)  # Replace 'None' with your default value or handling for missing 'id'
        print(f"id{user_id}")
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status=400)

        # Fetch the user profile based on the user ID
        user_profile = UserProfile.objects.get(id=user_id)
        user_profile_data = user_profile_to_dict(user_profile)
        return JsonResponse({'user': user_profile_data})
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User profile not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
