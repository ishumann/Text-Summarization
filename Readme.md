# End to end Text-Summarizer-Project

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ishumann/Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n nlpproj python=3.10 -y
```

```bash
conda activate nlpproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Ishuman Agrawal
Occupation: Data Scientist
Email: mann.agrawal17@gmail.com

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment #with specific access

	

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

![](/readme_img/iam.png)
![](/readme_img/access_key.png)
![](/readme_img/access_key_2.png)
![](/readme_img/access_key_3.png)
![](/readme_img/access_key_4.png)

![](/readme_img/set_permissions.png)
![](/readme_img/set_permissions_2.png)
![](/readme_img/set_permissions_3.png)



## 3. Create ECR repo to store/save docker image
	1. ECR: Elastic Container registry to save your docker image in aws
    
	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

![](/readme_img/ecr.png)
![](/readme_img/ecr2.png)
![](/readme_img/ecr3.png)
![](/readme_img/ecr4.png)

    - Save the URI: 050407812497.dkr.ecr.us-east-1.amazonaws.com/text-s
	
## 4. Create EC2 machine (Ubuntu) 

	2. EC2 access : It is virtual machine
![](/readme_img/ec2.png)
![](/readme_img/ec22.png)
![](/readme_img/ec23.png)
![](/readme_img/ec24.png)
![](/readme_img/ec25.png)

## 5. Open EC2 and Install docker in EC2 Machine:
	

![](/readme_img/ec2_install_and_config.png)
![](/readme_img/ec2_install_and_config2.png)

	#optional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

![](/readme_img/ec2_install_and_config3.png)
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

![](/readme_img/gitaction.png)

	Copy the runner commands and configuration code and paste and execute it in the ec2 instance terminal one by one.

![](/readme_img/gitaction2.png)
![](/readme_img/gitaction3.png)

	To turn gitaction offline to idle state, execute "./run.sh" on ec2 terminal

# 7. Setup github secrets:

![](/readme_img/secrets.png)

	secrets keys are provided in the csv file you downloaded

![](/readme_img/access_key_4.png)
![](/readme_img/secrets2.png)

    AWS_ACCESS_KEY_ID  #depends on your key

    AWS_SECRET_ACCESS_KEY #depends on your key

    AWS_REGION  us-east-1 # depends on your region

    AWS_ECR_LOGIN_URI  	#depends on your URI

    ECR_REPOSITORY_NAME = text-s #depends on your repository name

# 8 Push the code to github

![](/readme_img/CICD.png)
![](/readme_img/CICD2.png)
![](/readme_img/CICD3.png)
	
# 9. Configure Port Mapping in EC2

![](/readme_img/portmapping.png)
![](/readme_img/portmapping2.png)
![](/readme_img/portmapping3.png)
![](/readme_img/portmapping4.png)
![](/readme_img/portmapping5.png)
![](/readme_img/portmapping5.png)


# 10. Finally 

Open the public IP of your EC2 instance in the browser to see the deployed application.

![](/readme_img/final.png)

