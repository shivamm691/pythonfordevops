import boto3  # Import the Boto3 library for AWS API access

def list_iam_users():
    """
    List all IAM users in the AWS account.
    """
    iam_client = boto3.client('iam')  # Create a new IAM client

    try:
        # Call the list_users method to get a list of all IAM users
        response = iam_client.list_users()
        users = response['Users']  # Extract the list of users from the response

        if not users:
            print("No IAM users found.")
        else:
            # Print details of each user
            for user in users:
                print(f"User: {user['UserName']}, ARN: {user['Arn']}, Created on: {user['CreateDate']}")

    except Exception as e:
        print(f"Error listing IAM users: {e}")  # Handle any errors that occur

def list_iam_roles():
    """
    List all IAM roles in the AWS account.
    """
    iam_client = boto3.client('iam')  # Create a new IAM client

    try:
        # Call the list_roles method to get a list of all IAM roles
        response = iam_client.list_roles()
        roles = response['Roles']  # Extract the list of roles from the response

        if not roles:
            print("No IAM roles found.")
        else:
            # Print details of each role
            for role in roles:
                print(f"Role: {role['RoleName']}, ARN: {role['Arn']}, Created on: {role['CreateDate']}")

    except Exception as e:
        print(f"Error listing IAM roles: {e}")  # Handle any errors that occur

def list_iam_groups():
    """
    List all IAM user groups in the AWS account.
    """
    iam_client = boto3.client('iam')  # Create a new IAM client

    try:
        # Call the list_groups method to get a list of all IAM groups
        response = iam_client.list_groups()
        groups = response['Groups']  # Extract the list of groups from the response

        if not groups:
            print("No IAM groups found.")
        else:
            # Print details of each group
            for group in groups:
                print(f"Group: {group['GroupName']}, ARN: {group['Arn']}, Created on: {group['CreateDate']}")

    except Exception as e:
        print(f"Error listing IAM groups: {e}")  # Handle any errors that occur

if __name__ == "__main__":
    # Main function to call the above functions and list IAM resources
    print("Listing IAM Users:")
    list_iam_users()  # List all IAM users
    print("\nListing IAM Roles:")
    list_iam_roles()  # List all IAM roles
    print("\nListing IAM Groups:")
    list_iam_groups()  # List all IAM groups
