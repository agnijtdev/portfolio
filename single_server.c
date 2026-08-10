#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<arpa/inet.h>

int main(){
    char *ip="127.0.0.0";
    int port=5567;
    int server_sock,client_sock;
    struct sockaddr_in server_addr,client_addr;
    socklen_t addr_size;
    int n;
    char buffer[1024];
    server_sock=socket(AF_INET,SOCK_STREAM,0);

    memset(&server_addr,'\0',sizeof(server_addr));
    server_addr.sin_family=AF_INET;
    server_addr.sin_port=htons(port);
    server_addr.sin_addr.s_addr=inet_addr(ip);

    n=bind(server_sock,(struct sockaddr*)&server_addr,sizeof(server_addr));
    if(n<0){
        printf("[-]Bind failed\n");
        exit(0);
    }
    printf("[+]Bind succesfull to port number %d \n",port);
    listen(server_sock,10);
    printf("listining \n");
    while(1) {
        
    }


}