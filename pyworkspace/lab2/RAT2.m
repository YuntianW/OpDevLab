%% R,A,T, calcualte films reflelectance, absorption and transmittance

%%%%%%%%%% refraction intex Vs wavelenge %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

[lamda1,nalq,kalq]=textread('Lab2-nk-Alq.txt','%d %f %f',-1);
[lamda1,nag,kag]=textread('Lab2-nk-Ag.txt','%d %f %f',-1);
[lamda1,nglass,kglass]=textread('Lab2-nk-glass.txt','%d %f %f',-1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Nalq=nalq+i*kalq;
Nag=nag+i*kag;
Nglass=nglass+i*kglass;


for a=1:1:length(lamda1);
   
    lamda=lamda1(a);
    

N=[1 Nag(a) Nalq(a) Nag(a) Nglass(a)];
d=[  20 100 100 ];

layer=3;


S=[1 0;0 1];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 for p=1:layer         %算每一层的L、I矩阵元素
           r(p)=(N(p)-N(p+1))/(N(p)+N(p+1));
           t(p)=2*N(p)/(N(p)+N(p+1));
           I(:,:)=(1/t(p))*[1 r(p);r(p) 1];
           L(:,:)=[exp(-i*2*pi*N(p+1)*d(p)/lamda) 0;0 exp(i*2*pi*N(p+1)*d(p)/lamda)];
           S=S*I(:,:)*L(:,:);
 end
           r(p+1)=(N(p+1)-N(p+2))/(N(p+1)+N(p+2));      %算最后一个I矩阵
           t(p+1)=2*N(p+1)/(N(p+1)+N(p+2));
           I(:,:)=1/t(p+1)*[1 r(p+1);r(p+1) 1];
           S=S*I(:,:);
           
         
            
            R(a)=(abs(S(2,1)/S(1,1)))^2; 
            T(a)=(1/(S(1,1)*conj(S(1,1))))*N(p+2)/N(1);
            Ab(a)=1-R(a)-T(a);           
           
           
        end



x=R';
y=Ab';
z=T';
m=lamda1;
save x.txt x -ascii;
save y.txt y -ascii;
save z.txt z -ascii;
save m.txt m -ascii


%-----------------------------------------------plot

figure;
plot(lamda1,R,'ro-', lamda1,Ab,'gx',lamda1,T, 'bs-');grid on;
xlabel('Wavelength (nm)');ylabel('Spectrum');title('Spectrum');
legend('R','A','T');

