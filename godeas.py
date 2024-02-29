dati_file = input()
import numpy as np  
import matplotlib                                      
import matplotlib.pyplot as plt                                                 
import matplotlib.colors as cls                                                 
import matplotlib.patches as pts
dati = np.loadtxt(dati_file,delimiter=' ',usecols=(0,1,4,8,12),unpack=True)
fig,ax = plt.subplots(1,3,width_ratios=np.array([0.4,0.3,0.3]),figsize=(12,6))
N = len(dati[0])
m = 35
ax[0].set_xlim(-0.1,1.)
ax[0].set_ylim(8.4,-4.)
ax[2].set_xlim(0,4)
ax[0].set_xlabel('b-y')
ax[0].set_ylabel('$M_v$')
ax[1].set_xlabel('MsuH')
ax[2].set_xlabel('$M_{ini}$')
ax[2].set_ylabel('MsuH')
ax[2].yaxis.tick_right()
ages = np.sort(dati[4])
lim = np.zeros(m+1)
lim[0] = ages[0]
color = matplotlib.colormaps['turbo'](np.linspace(0,1,m))
for i in range(1,m+1):
    lim[i] = ages[int((i)*N/m)-1]
    ind = np.where((dati[4]<lim[i])&(dati[4]>lim[i-1]))
    ax[0].scatter(dati[3][ind],dati[2][ind],color=color[i-1],s=0.1,label="{} Gyr - {} Gyr".format(round(lim[i-1],2),round(lim[i],2)))
N = 30 
ind = [np.where(dati[4]<1),np.where((dati[4]>=1)&(dati[4]<=5)),np.where(dati[4]>5)]
age = [np.sort(dati[1][ind[0]]),np.sort(dati[1][ind[1]]),np.sort(dati[1][ind[2]])]
met = [dati[0][ind[0]],dati[0][ind[1]],dati[0][ind[2]]]
mas = [dati[1][ind[0]],dati[1][ind[1]],dati[1][ind[2]]]
lim = ['< 1 Gyr','1-5 Gyr','> 5 Gyr']                           
col = ['y','red','c']
color = ['Oranges','Blues','Greens']
c = ['orange','blue','green']
legenda = []
for i in range(3):
    a =  np.sort(met[i])
    media = np.sum(met[i])/len(met[i])
    mediana = a[int(len(met[i])/2)]
    ax[1].hist(met[i],bins=int((a[-1]-a[0])/0.2),color=col[i],label='{}'.format(lim[i]),density=True,alpha=0.3,histtype='stepfilled',ec='k')
    ax[1].axvline(x=media,linestyle='dashed',color=col[i],alpha=0.6,label='average')
    ax[1].axvline(x=mediana,linestyle='dotted',color=col[i],alpha=0.6,label='median')
    ist,xlim,ylim = np.histogram2d(mas[i],met[i],bins=[N,N//2],density = True,range=[[0,np.max(dati[1])],[np.min(dati[0]),np.max(dati[0])]])
    x = (xlim[:-1]+xlim[1:])/2
    y = (ylim[:-1]+ylim[1:])/2
    legenda = legenda + [pts.Patch(color=c[i],label=lim[i])]
    ax[2].contour(x,y,ist.T,cmap=color[i],alpha=0.5,linewidths=0.8)
    ax[2].contourf(x,y,ist.T,cmap=color[i],alpha=0.4,extend='min')
ax[0].legend(fontsize=4.5,scatterpoints=3)
ax[1].legend()
ax[2].legend(handles = legenda,loc='lower right')
plt.savefig('grafico_godeas.jpg')
plt.show()
