%% EXPORT GAIN
 clear;clc;
 dat=dlmread('C:\Users\scdb\Desktop\hornCalib3-6GHz.trx','',36,0);
 % FORMAT OF FILE
%Re H -- Im H -- Re V -- Im V
% 15 lines per azimuth position (line 1 to line 15)

maxL=length(dat(:,1))-120; %80 samples, every 2.5 MHz
j=1;

for k=1:120:maxL

pos=[1 16 31 46 61 76 91 106]; % Takes all these positions, then next frequency
pos=pos+k-1;

theta= ([24*2*pi/360/2:24*2*pi/360:2*pi-24*2*pi/360/2])';

for i=1:1:8
    figure(1);
subplot(4,2,i); 
Hpol=dat(pos(i):pos(i)+14,1).^2+dat(pos(i):pos(i)+14,2).^2; % power
plot(Hpol); hold on;
Vpol=dat(pos(i):pos(i)+14,3).^2+dat(pos(i):pos(i)+14,4).^2; % power
plot(Vpol,'r');
legend('Horizontal','Vertical')
    figure(2);
subplot(4,2,i); 
polar(theta,sqrt(Vpol(1:15)),'r'); hold on ; % field magnitude
polar(theta,sqrt(Hpol(1:15)));  % field magnitude
legend('Vertical','Horizontal')

Vpol_m(i)=max(Vpol);
Hpol_m(i)=max(Hpol);
end
Vpol_max(j)=max(Vpol_m);
Hpol_max(j)=max(Hpol_m);

j=j+1;

end 

Gain_table(:,1)=1:120:maxL;
Gain_table(:,2)=Vpol_max;
Gain_table(:,3)=Hpol_max;
Gain_table

%% PLUS FORM BOYAN SFS, if needed

%                             % Reshaping into Etheta and Ephi
%                             GTHtemp = (10.^(dat(:,4)/10)); 
%                             ThPhase = dat(:,5);
%                             GPHtemp = (10.^(dat(:,6)/10));
%                             PhPhase = dat(:,7);
%                             
%                             % Converting to E fields
%                             Etheta = sqrt(GTHtemp).*exp(1i.*ThPhase.*pi/180); 
%                             Ephi   = sqrt(GPHtemp).*exp(1i.*PhPhase.*pi/180);
