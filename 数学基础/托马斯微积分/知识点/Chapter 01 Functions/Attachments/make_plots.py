import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT=Path('/mnt/data/function_solutions_assets')
BLUE='#049DDB'
RED='#E74C3C'
ORANGE='#F5A623'
GRAY='#555555'

def setup(xlim, ylim, xlabel='x', ylabel='y', figsize=(4.2,3.0)):
    fig, ax=plt.subplots(figsize=figsize, dpi=220)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none'); ax.spines['top'].set_color('none')
    ax.spines['left'].set_linewidth(0.9); ax.spines['bottom'].set_linewidth(0.9)
    ax.grid(True, linewidth=0.35, alpha=0.25)
    ax.tick_params(labelsize=8, length=3)
    ax.set_xlabel(xlabel, loc='right', fontsize=9, labelpad=-2)
    ax.set_ylabel(ylabel, loc='top', fontsize=9, rotation=0, labelpad=-2)
    return fig, ax

def save(fig, name):
    fig.tight_layout(pad=0.45)
    fig.savefig(OUT/name, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def closed(ax,x,y,c=BLUE,s=28): ax.scatter([x],[y],s=s,c=c,zorder=5)
def openpt(ax,x,y,c=BLUE,s=30): ax.scatter([x],[y],s=s,facecolors='white',edgecolors=c,linewidths=1.3,zorder=6)

# 15
fig,ax=setup((-3,5),(-5,9)); x=np.linspace(-3,5,400); ax.plot(x,5-2*x,color=BLUE,lw=2); save(fig,'g15.png')
#16
fig,ax=setup((-5,3),(-8,4)); x=np.linspace(-5,3,500); ax.plot(x,1-2*x-x*x,color=BLUE,lw=2); ax.scatter([-1],[2],c=RED,s=24); save(fig,'g16.png')
#17
fig,ax=setup((-5,5),(-0.5,2.7)); x=np.linspace(-5,5,500); ax.plot(x,np.sqrt(np.abs(x)),color=BLUE,lw=2); save(fig,'g17.png')
#18
fig,ax=setup((-6,2),(-0.5,3)); x=np.linspace(-6,0,400); ax.plot(x,np.sqrt(-x),color=BLUE,lw=2); closed(ax,0,0); save(fig,'g18.png')
#19
fig,ax=setup((-4,4),(-2,2)); x1=np.linspace(-4,-.03,300); x2=np.linspace(.03,4,300); ax.plot(x1,-np.ones_like(x1),color=BLUE,lw=2); ax.plot(x2,np.ones_like(x2),color=BLUE,lw=2); openpt(ax,0,-1); openpt(ax,0,1); save(fig,'g19.png')
#20
fig,ax=setup((-5,5),(-0.5,6)); x1=np.linspace(-5,-.18,500); x2=np.linspace(.18,5,500); ax.plot(x1,1/np.abs(x1),color=BLUE,lw=2); ax.plot(x2,1/np.abs(x2),color=BLUE,lw=2); ax.axvline(0,color=GRAY,lw=.8,ls='--'); save(fig,'g20.png')

# 23a |y|=x
fig,ax=setup((-1,5),(-4,4)); x=np.linspace(0,5,400); ax.plot(x,x,color=BLUE,lw=2); ax.plot(x,-x,color=BLUE,lw=2); save(fig,'g23a.png')
# 23b y^2=x^2
fig,ax=setup((-4,4),(-4,4)); x=np.linspace(-4,4,400); ax.plot(x,x,color=BLUE,lw=2); ax.plot(x,-x,color=BLUE,lw=2); save(fig,'g23b.png')
#24a diamond
fig,ax=setup((-1.5,1.5),(-1.5,1.5)); xx=np.array([-1,0,1,0,-1]); yy=np.array([0,1,0,-1,0]); ax.plot(xx,yy,color=BLUE,lw=2); save(fig,'g24a.png')
#24b x+|y|=1
fig,ax=setup((-3,2),(-4,4)); x=np.linspace(-3,1,400); ax.plot(x,1-x,color=BLUE,lw=2); ax.plot(x,x-1,color=BLUE,lw=2); save(fig,'g24b.png')

# 25
fig,ax=setup((-.4,2.4),(-.3,1.4)); x=np.linspace(0,1,200); ax.plot(x,x,color=BLUE,lw=2); x=np.linspace(1,2,200); ax.plot(x,2-x,color=BLUE,lw=2); closed(ax,0,0); closed(ax,1,1); closed(ax,2,0); save(fig,'g25.png')
#26
fig,ax=setup((-.4,2.4),(-.3,1.4)); x=np.linspace(0,1,200); ax.plot(x,1-x,color=BLUE,lw=2); x=np.linspace(1.01,2,200); ax.plot(x,2-x,color=BLUE,lw=2); closed(ax,0,1); closed(ax,1,0); openpt(ax,1,1); closed(ax,2,0); save(fig,'g26.png')
#27
fig,ax=setup((-3,4),(-8,15)); x=np.linspace(-3,1,400); ax.plot(x,4-x*x,color=BLUE,lw=2); x=np.linspace(1.01,4,400); ax.plot(x,x*x+2*x,color=BLUE,lw=2); closed(ax,1,3); openpt(ax,1,3); save(fig,'g27.png')
#28
fig,ax=setup((-5,5),(-5,5)); x=np.linspace(-5,-.15,500); ax.plot(x,1/x,color=BLUE,lw=2); x=np.linspace(0,5,300); ax.plot(x,x,color=BLUE,lw=2); closed(ax,0,0); ax.axvline(0,color=GRAY,lw=.8,ls='--'); save(fig,'g28.png')

#36 integer part (truncate)
fig,ax=setup((-4.2,4.2),(-4.2,4.2));
for n in range(0,4):
    ax.plot([n,n+1],[n,n],color=BLUE,lw=2); closed(ax,n,n); openpt(ax,n+1,n)
for n in range(-4,0):
    # ceil(x)=n on (n-1,n]
    ax.plot([n-1,n],[n,n],color=BLUE,lw=2); openpt(ax,n-1,n); closed(ax,n,n)
closed(ax,0,0)
save(fig,'g36.png')

#37
fig,ax=setup((-2.2,2.2),(-9,9)); x=np.linspace(-2.1,2.1,500); ax.plot(x,-x**3,color=BLUE,lw=2); save(fig,'g37.png')
#38
fig,ax=setup((-4,4),(-8,1)); x1=np.linspace(-4,-.35,500); x2=np.linspace(.35,4,500); ax.plot(x1,-1/x1**2,color=BLUE,lw=2); ax.plot(x2,-1/x2**2,color=BLUE,lw=2); ax.axvline(0,color=GRAY,lw=.8,ls='--'); save(fig,'g38.png')
#39
fig,ax=setup((-5,5),(-5,5)); x1=np.linspace(-5,-.2,500); x2=np.linspace(.2,5,500); ax.plot(x1,-1/x1,color=BLUE,lw=2); ax.plot(x2,-1/x2,color=BLUE,lw=2); ax.axvline(0,color=GRAY,lw=.8,ls='--'); save(fig,'g39.png')
#40
fig,ax=setup((-5,5),(-.5,6)); x1=np.linspace(-5,-.18,500); x2=np.linspace(.18,5,500); ax.plot(x1,1/np.abs(x1),color=BLUE,lw=2); ax.plot(x2,1/np.abs(x2),color=BLUE,lw=2); ax.axvline(0,color=GRAY,lw=.8,ls='--'); save(fig,'g40.png')
#41
fig,ax=setup((-5,5),(-.5,2.7)); x=np.linspace(-5,5,500); ax.plot(x,np.sqrt(np.abs(x)),color=BLUE,lw=2); save(fig,'g41.png')
#42
fig,ax=setup((-6,2),(-.5,3)); x=np.linspace(-6,0,400); ax.plot(x,np.sqrt(-x),color=BLUE,lw=2); closed(ax,0,0); save(fig,'g42.png')
#43
fig,ax=setup((-.5,6),(-.5,2.3)); x=np.linspace(0,6,500); ax.plot(x,x**(3/8),color=BLUE,lw=2); closed(ax,0,0); save(fig,'g43.png')
#44
fig,ax=setup((-.5,6),(-11,1)); x=np.linspace(0,6,500); ax.plot(x,-4*np.sqrt(x),color=BLUE,lw=2); closed(ax,0,0); save(fig,'g44.png')
#45
fig,ax=setup((-.5,5),(-12,1)); x=np.linspace(0,5,500); ax.plot(x,-x**1.5,color=BLUE,lw=2); closed(ax,0,0); save(fig,'g45.png')
#46
fig,ax=setup((-5,5),(-.5,3.5)); x=np.linspace(-5,5,500); ax.plot(x,np.abs(x)**(2/3),color=BLUE,lw=2); save(fig,'g46.png')

#71 comparison
fig,ax=setup((-6,8),(-8,8));
x1=np.linspace(-6,-.35,500); x2=np.linspace(.35,8,500); x=np.linspace(-6,8,500)
ax.plot(x,x/2,color=BLUE,lw=2,label=r'$x/2$'); ax.plot(x1,1+4/x1,color=ORANGE,lw=2,label=r'$1+4/x$'); ax.plot(x2,1+4/x2,color=ORANGE,lw=2); ax.axvline(0,color=GRAY,lw=.8,ls='--'); ax.legend(fontsize=8,frameon=False); save(fig,'g71.png')
#72 comparison
fig,ax=setup((-8,6),(-8,8));
for a,b in [(-8,-1.15),(-.85,.85),(1.15,6)]:
    x=np.linspace(a,b,500); ax.plot(x,3/(x-1),color=BLUE,lw=2)
for a,b in [(-8,-1.15),(-.85,.85),(1.15,6)]:
    x=np.linspace(a,b,500); ax.plot(x,2/(x+1),color=ORANGE,lw=2)
ax.axvline(-1,color=GRAY,lw=.8,ls='--'); ax.axvline(1,color=GRAY,lw=.8,ls='--');
ax.plot([],[],color=BLUE,lw=2,label=r'$3/(x-1)$'); ax.plot([],[],color=ORANGE,lw=2,label=r'$2/(x+1)$'); ax.legend(fontsize=8,frameon=False); save(fig,'g72.png')

print('generated',len(list(OUT.glob('g*.png'))),'plots')
