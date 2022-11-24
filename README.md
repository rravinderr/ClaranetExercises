# ClaranetExercises

Claranet Exercises - deadline 23_11_2022


## Some comments - exercise 4: 

This was my very first project of this kind. Very interesting!
Although it gave me the possibility to learn a lot, the project is partially completed:
it creates the instances on AWS, but configuration part is not complete.

## IDEA:

The idea consists in using both Ansible and Cloudformation for this project to 
achieve the goal of automating both the creation of the infrustrcture and setup
of the application. Specifically: Ansible for configuration management and 
Cloudformation for provisioning resources.

EC2 instances + a load balancer and a cluster of RDS are needed to meet 
the need of being fault-tolerant & adaptive.

## To run the playbook:

 - edit group_vars/* files according your own setup
 - run aws_ac_wordpress.yml playbook as the following:
    
    ansible-playbook -i inventory aws_ac_wordpress.yml


For the testing I used AWS Free Tier.
