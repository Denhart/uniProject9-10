%script needs to be in SAtimo folder !
fhandle=@Satimo_measEff;
for i=1:1:20
[f(:,i) effdB(:,i)]=fhandle(strcat('M:\Private\MyProjects\ICEAA\600\measTun\',num2str(i),'.trx'),'L'); %specify low band or high band for Cal_table
end
close all

figure('Name','Final');
set( axes('FontSize',14));
for i=1:1:14
    plot(f(:,i),effdB(:,i));hold on;
end
xlabel('Frequency [MHz]','interpreter','latex','FontSize',14);
ylabel('$\eta_{T}$','interpreter','latex','FontSize',14);
ylim([-15 0]);