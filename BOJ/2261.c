// quick sort worst case O(n^2) TLE 실패
#include <stdio.h>
#include <stdlib.h>
#define min(a,b) ((a)<(b)?(a):(b))

struct point
{
    int x;
    int y;
};

int dist(struct point a,struct point b){
    return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);
}
int cmpx(const void* a,const void* b){
    return ((struct point*)a)->x - ((struct point*)b)->x;
}
int cmpy(const void* a,const void* b){
    return ((struct point*)a)->y - ((struct point*)b)->y;
}
int ClosestPair(struct point* p,int n);

int main()
{
    int n;
    scanf("%d",&n);

    struct point* p = (struct point*)malloc(n*sizeof(struct point));
    for(int i=0;i<n;i++)
        scanf("%d %d",&p[i].x,&p[i].y);
    qsort(p,n,sizeof(struct point),cmpx);

    printf("%d\n",ClosestPair(p,n));
    
    free(p);
    return 0;
}

int ClosestPair(struct point* p,int n)
{
    if (n==2)
    {
        return dist(p[0],p[1]);
    }
    else if (n==3)
    {
        int mindist = dist(p[0],p[1]);
        mindist = min(dist(p[0],p[2]),mindist);
        mindist = min(dist(p[1],p[2]),mindist);
        return mindist;
    }

    int mid = n/2;
    int mindist = min(ClosestPair(p,mid),ClosestPair(p+mid,n-mid));
    
    struct point* q = (struct point*)malloc((n)*sizeof(struct point));
    int count = 0;
    for (int i=0;i<n;i++){
        if ((p[i].x-p[mid].x)*(p[i].x-p[mid].x) < mindist){
            q[count++] = p[i];
        }
    }
    qsort(q,count,sizeof(struct point),cmpy);

    for (int i=0;i<count;i++){
        for (int j=i+1;j<count && (q[j].y-q[i].y)*(q[j].y-q[i].y) < mindist;j++){
            mindist = min(mindist,dist(q[i],q[j]));
        }
    }

    free(q);
    return mindist;
}