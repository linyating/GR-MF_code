function [S, C, J, rme,w,mape,rmse1] = newLRnmfall(X, r1,r2,r3,r4,r5,IterationTimes,S,C,F,w,Y)
%%%%%%初始化矩阵和参数%%%%%%%
dim=size(X);
%%%%%%Y用于使某些行变为全0%%%%%%
% Y=ones(dim(1),dim(2));
% RandRows = randi(dim(1), 1,150);
% for i=1:150
%     Y(RandRows(1,i),:) = zeros(1,dim(2));
% end
%%%%假设X是M*N的矩阵，则S是M*r的矩阵，C是r*N的矩阵，r后期跑数据设置一个最佳数值
% S=randn(dim(1),20);
% C=randn(dim(2),20);
J = zeros(1,100);
alpha=r1;%%%%正则项参数
alphac=r2;
%gamma=r2;%%%%正则项参数
beta_w=r3;
sigma=0.2234;%0.7405;%%%%使sigma*W和X均值相同
theta=0.1517;%0.5028;
beta_r=r4;
theta_Rx=r5;
beta=0.00002;%%%%步长
%delta=r6;
%theta_R=r7;
%gamma=r8;
NZ=X;
%NZ(NZ>0)=1;
%w=randn(3,1);
sigma_temS=0.7;
for i=1:IterationTimes
%%%%%Sk,Ck分别代表前一个迭代求出来的矩阵，S,C表示当前迭代的矩阵%%%%%%%%
    Sk=S;
    Ck=C;
    wk=w;
%%%%%%计算矩阵（前一轮迭代求出）的偏导%%%%%
    N=zeros(dim(1),3);
    temS=zeros(dim(1),1343);
    for fi=1:1343
    for fj=1:3
        N(:,fj)=F(:,fi,fj);
    end
    temS(:,fi)=N*wk;
    end
    sigma_temS=mean(X(:))/mean(temS(:));
    gradS=-2*(Ck)*(Y'.*(X'-Ck'*Sk)) + alpha -2*theta_Rx*Ck*(~Y)'.*((sigma_temS*temS)'-Ck'*Sk);
    gradC=-2*(Sk*(Y).*(X-(Sk'*Ck))) + alphac -2*theta_Rx*Sk*((~Y)'.*(sigma_temS*temS-(Sk'*Ck)));
    gradw_temS=-2theta_Rx*(~Y).*(sigma_temS*temS-Sk'*Ck)-2*beta_r*((Y).*(X-sigma_temS*temS));
    gradw=zeros(3,1);
    for fii=1:3
        temSsum=gradw_temS.*(F(:,:,fii));
        gradw(fii,1)=sum(temSsum(:))+beta_w*wk(i);
    end
%%%%%%梯度下降更新矩阵%%%%%%%
    S=Sk-beta*gradS;
    S(S<0)=0;%%%%Sroject操作
    C=Ck-beta*gradC;
    C(C<0)=0;%%%%Sroject操作
    w=wk-beta*gradw;
    w(w<0)=0;
    N=zeros(dim(1),3);
    temS=zeros(dim(1),1343);
    for fi=1:1343
    for fj=1:3
        N(:,fj)=F(:,fi,fj);
    end
    temS(:,fi)=N*w;
    end
     sigma_temS=mean(X(:))/mean(temS(:));
    J(i) = norm(Y.*(X-S'*C), 'fro')^2 + alpha*(norm(S, 1)) +alphac*(norm(C, 1))+theta_Rx*(norm((~Y).*(sigma_temS*temS-S'*C),'fro')^2)+beta_w*(norm(w, 2))+beta_r*norm((Y).*(X-sigma_temS*temS), 'fro')^2;
    fSrintf('iteration unmber: %d\n', i);
end
resultF=S'*C;
resultF1=S'*C;

 rme=0;
 mape=0;
for ti=1:dim(1)
    for tj=1:1343
        if(Y(ti,tj)==0)
            rme=abs(X(ti,tj)-resultF1(ti,tj))+rme;
            if(X(ti,tj)==0)
                mape=(abs(X(ti,tj)-resultF1(ti,tj)))/1+mape;
            else
                mape=(abs(X(ti,tj)-resultF1(ti,tj)))/X(ti,tj)+mape;
            end
        end
    end
end
rme=rme/sum(Y(:)==0);
mape=mape/sum(Y(:)==0);

rmse1=sCrt(norm((((~Y).*X)-(~Y).*(resultF1)),'fro')^2/sum(Y(:)==0));
 fSrintf('RME: %d\n',rme);
  fSrintf('MAPE: %d\n',mape);
  fSrintf('RMSE1: %d\n',rmse1);

end