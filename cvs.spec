#
# Conditional build:
%bcond_with	kerberos5	# enable kerberos5 support
#
Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(es):	Control de versiones en modo concurrente
Summary(fr):	Un système pour maintenir à jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(pt_BR):	Controle de versões em modo concorrente
Summary(ru):	óÉÓÔÅÍÁ ÕÐÒÁ×ÌÅÎÉÑ ×ÅÒÓÉÑÍÉ
Summary(tr):	Sürüm denetim sistemi
Summary(uk):	óÉÓÔÅÍÁ ËÅÒÕ×ÁÎÎÑ ×ÅÒÓ¦ÑÍÉ
Summary(zh_CN):	²¢·¢µÄ°æ±¾¹ÜÀíÏµÍ³CVS
Name:		cvs
Version:	1.11.17
Release:	1
License:	GPL
Group:		Development/Version Control
# new feature release: http://ftp.cvshome.org/release/feature/cvs-1.12.5/cvs-1.12.5.tar.bz2
Source0:	http://ccvs.cvshome.org/files/documents/19/191/%{name}-%{version}.tar.bz2
# Source0-md5:	17cd48888d5571d215a44a7e8d46759c
Source1:	%{name}.inetd
# based on:	http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/cvs-1.11.2-20020513-ipv6.patch.gz
Patch0:		%{name}-ipv6.patch
Patch1:		%{name}-zlib.patch
Patch2:		%{name}-fixed_buffer.patch
Patch3:		%{name}-cvspass.patch
Patch4:		%{name}-home_etc.patch
Patch5:		%{name}-newnline.patch
Patch6:		%{name}-no_libnsl.patch
Patch7:		%{name}-info.patch
URL:		http://www.cyclic.com/
# should be 2.58/1.7.9 resp.
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7.6
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	zlib-devel
Obsoletes:	cvs-nserver-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvs_root	/home/cvsroot

%description
CVS means Concurrent Version System; it is a version control system
which can record the history of your files (usually, but not always,
source code). CVS only stores the differences between versions,
instead of every version of every file you've ever created. CVS also
keeps a log of who and when made some changes and why they occurred,
among other aspects.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
Überwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software-Entwickler notwendig sind.

%description -l es
CVS significa "Concurrent Version System" (sistema concurrente de
control de versiones). Puede guardar la historia de sus ficheros
(normalmente, pero no necesariamente, código fuente). CVS sólo guarda
las diferencias entre las versiones, en vez de guardar cada una de las
versiones de cada fichero que haya creado. CVS también mantiene un
registro de quién y cuándo realizó un cambio, el porqué del cambio,
etc.

CVS es muy útil para manejar los releases y controlar la edición
concurrente de los ficheros fuente entre varios autores. En vez de
proveer control de versiones para una colección de ficheros en un solo
directorio, CVS la provee para una colección jerárquica de directorios
que consistan de ficheros de revisiones controladas. Esos directorios
y ficheros pueden luego ser reunidos para formar un release de
software.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un système de
comparaison de versions de fichiers, qui peut garder une trace des
changements apportés à des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les différences, et
non l'intégralité d'un fichier récent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date à laquelle celle-ci a eu lieu.

CVS est très utile pour gérer la mise en commun des modifications
apportées par plusieurs personnes travaillant en parallèle sur les
mêmes fichiers. Au lieu de garder plusieurs versions des fichiers dans
un seul répertoire, CVS crée une série de répertoires, chacun
contenant une nouvelle version des fichiers. Ces répertoires et ces
fichiers peuvent ensuite être regroupés pour former la version la plus
à jour du logiciel. Installez ce package si vous avez besoin
d'utiliser un système de contrôle de version.

%description -l pl
CVS jest nak³adk± na rcs (Revision Control System, czyli w wolnym
t³umaczeniu system kontroli wersji zasobów), który rozszerza
mo¿liwo¶ci rcs'a z narzêdzia do kontroli zbioru plików w pojedynczym
katalogu o mo¿liwo¶æ kontroli zbioru hierarchicznie u³o¿onych
katalogów z plikami. Z pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem
¼ród³owym opracowywanym przez nawet bardzo du¿e zespo³y programistów
umo¿liwiaj±c ¶ledzenie i kontrolê wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe³nych wersji oprogramowania (release).

%description -l pt_BR
CVS é um front end para o rcs(1) - revision control system - que
estende a noção de controle de revisão de uma coletânea de arquivo em
um único diretório para uma coleção hierárquica de diretórios que
contém arquivos controlados por revisão. Esses diretórios e arquivos
podem ser combinados juntos para criar uma release de software. CVS
oferece as funções necessárias para administrar essas release de
software e para controlar a edição concorrente de arquivos fonte por
múltiplos programadores.

%description -l ru
CVS (Concurrent Version System) - ÜÔÏ ÓÉÓÔÅÍÁ ÕÐÒÁ×ÌÅÎÉÑ ×ÅÒÓÉÑÍÉ,
ËÏÔÏÒÁÑ ÕÍÅÅÔ ÚÁÐÉÓÁÔØ ÉÓÔÏÒÉÀ ×ÁÛÉÈ ÆÁÊÌÏ× (ÏÂÙÞÎÏ, ÎÏ ÎÅ ×ÓÅÇÄÁ, ÜÔÏ
ÉÓÈÏÄÎÙÅ ÔÅËÓÔÙ). CVS ÓÏÈÒÁÎÑÅÔ ÔÏÌØËÏ ÒÁÚÌÉÞÉÑ ÍÅÖÄÕ ×ÅÒÓÉÑÍÉ ×ÍÅÓÔÏ
ËÁÖÄÏÊ ×ÅÒÓÉÉ ËÁÖÄÏÇÏ ÆÁÊÌÁ, ËÏÔÏÒÁÑ ÂÙÌÁ ËÏÇÄÁ-ÌÉÂÏ ÓÏÚÄÁÎÁ. ôÁËÖÅ
CVS ÈÒÁÎÉÔ ÐÒÏÔÏËÏÌ ÔÏÇÏ, ËÔÏ, ËÏÇÄÁ É ÚÁÞÅÍ ÞÔÏ-ÌÉÂÏ ÉÚÍÅÎÉÌ.

CVS ÏÞÅÎØ ÐÏÌÅÚÎÁ ÄÌÑ ÏÒÇÁÎÉÚÁÃÉÉ ÒÅÌÉÚÏ× É ÕÐÒÁ×ÌÅÎÉÑ ÐÁÒÁÌÌÅÌØÎÏÊ
ÐÒÁ×ËÏÊ ÉÓÈÏÄÎÙÈ ÆÁÊÌÏ× ÎÅÓËÏÌØËÉÍÉ Á×ÔÏÒÁÍÉ. ÷ÍÅÓÔÏ ÐÒÅÄÏÓÔÁ×ÌÅÎÉÑ
ÕÐÒÁ×ÌÅÎÉÑ ×ÅÒÓÉÑÍÉ ÎÁÂÏÒÁ ÆÁÊÌÏ× × ÏÄÎÏÍ ËÁÔÁÌÏÇÅ CVS ÐÒÅÄÏÓÔÁ×ÌÑÅÔ
ÕÐÒÁ×ÌÅÎÉÅ ×ÅÒÓÉÑÍÉ ÉÅÒÁÒÈÉÞÅÓËÏÇÏ ÎÁÂÏÒÁ ËÁÔÁÌÏÇÏ×, ÓÏÓÔÏÑÝÉÈ ÉÚ
ÆÁÊÌÏ×, ×ÅÒÓÉÑÍÉ ËÏÔÏÒÙÈ ÎÁÄÏ ÕÐÒÁ×ÌÌÑÔØ. üÔÉ ÆÁÊÌÙ É ËÁÔÁÌÏÇÉ ÍÏÇÕÔ
ÂÙÔØ ÓÏÂÒÁÎÙ ×ÍÅÓÔÅ ÄÌÑ ÆÏÒÍÉÒÏ×ÁÎÉÑ ÒÅÌÉÚÁ ðï.

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
topluluðunun sürüm denetimini, denetimi yapýlmýþ dizinlerin hiyerarþik
topluluðuna geniþleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu
dizin ve dosyalar, bir yazýlým yayýný oluþturma amacýyla biraraya
getirilebilir. CVS, bu yazýlým yayýnlarýnýn yönetilmesini ve kaynak
dosyalarý bakýmýnýn birden çok yazýlým geliþtiricisi tarafýndan
eþzamanlý olarak yapýlmasýný kontrol etmek için gereken iþlevleri
saðlar.

%description -l uk
CVS (Concurrent Version System) - ÃÅ ÓÉÓÔÅÍÁ ËÅÒÕ×ÁÎÎÑ ×ÅÒÓ¦ÑÍÉ, ÑËÁ
×Í¦¤ ÚÁÐÉÓÁÔÉ ¦ÓÔÏÒ¦À ×ÁÛÉÈ ÆÁÊÌ¦× (ÚÁÚ×ÉÞÁÊ, ÁÌÅ ÎÅ ÚÁ×ÖÄÉ, ÃÅ
×ÉÈ¦ÄÎ¦ ÔÅËÓÔÉ). CVS ÚÂÅÒ¦ÇÁ¤ Ô¦ÌØËÉ Ò¦ÚÎÉÃÀ Í¦Ö ×ÅÒÓ¦ÑÍÉ ÚÁÍ¦ÓÔØ
ËÏÖÎÏ§ ×ÅÒÓ¦§ ËÏÖÎÏÇÏ ÆÁÊÌÕ, ÑËÁ ÂÕÌÁ ËÏÌÉÓØ ÓÔ×ÏÒÅÎÁ. ôÁËÏÖ CVS
ÚÂÅÒ¦ÇÁ¤ ÐÒÏÔÏËÏÌ ÔÏÇÏ, ÈÔÏ, ËÏÌÉ ¦ ÎÁ×¦ÝÏ ÝÏÓØ ÚÍ¦ÎÉ×.

CVS ÄÕÖÅ ËÏÒÉÓÎÁ ÄÌÑ ÏÒÇÁÎ¦ÚÁÃ¦À ÒÅÌ¦Ú¦× ÔÁ ËÅÒÕ×ÁÎÎÑ ÐÁÒÁÌÅÌØÎÏÀ
ÐÒÁ×ËÏÀ ×ÉÚ¦ÄÎÉÈ ÆÁÊÌ¦× Ë¦ÌØËÏÍÁ Á×ÔÏÒÁÍÉ. úÁÍ¦ÓÔØ ÎÁÄÁÎÎÑ ÍÏÖÌÉ×ÏÓÔ¦
ËÅÒÕ×ÁÎÎÑ ×ÅÒÓ¦ÑÍÉ ÎÁÂÏÒÕ ÆÁÊÌ¦× × ÏÄÎÏÍÕ ËÁÔÁÌÏÚ¦, CVS ÎÁÄÁ¤
ÍÏÖÌÉ×¦ÓÔØ ËÅÒÕ×ÁÎÎÑ ¦¤ÒÁÒÈ¦ÞÎÉÍ ÎÁÂÏÒÏÍ ËÁÔÁÌÏÇ¦×, ÝÏ ÓËÌÁÄÁÀÔØÓÑ Ú
ÆÁÊÌ¦×, ×ÅÒÓ¦ÑÍÉ ËÏÔÒÉÈ ÔÒÅÂÁ ËÅÒÕ×ÁÔÉ. ã¦ ÆÁÊÌÉ ÔÁ ËÁÔÁÌÏÇÉ ÍÏÖÕÔØ
ÂÕÔÉ Ú¦ÂÒÁÎ¦ ÒÁÚÏÍ ÄÌÑ ÆÏÒÍÕ×ÁÎÎÑ ÒÅÌ¦ÚÕ ðú.

%package pserver
Summary:	rc-inetd config files to run CVS pserver
Summary(es):	Ficheros de configuración de rc-inetd para un servidor CVS pserver
Summary(pl):	Pliki konfiguracyjne rc-inetd do postawienia pservera CVS
Group:		Development/Version Control
PreReq:		%{name} = %{version}
PreReq:		rc-inetd
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post):	fileutils
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Obsoletes:	cvs-nserver-common
Obsoletes:	cvs-nserver-nserver
Obsoletes:	cvs-nserver-pserver

%description pserver
Config files for rc-inetd that are necessary to run CVS in pserver
mode.

%description pserver -l es
Los ficheros de configuración necesarios para ejecutar CVS en el modo
de pserver.

%description pserver -l pl
Pliki konfiguracyjne rc-inetd niezbêdne do uruchomienia CVSa w trybie
pserver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# seems not-so-really needed yet
%{__perl} -pi -e 's/(AC_PREREQ)\(2\.58\)/$1\(2.57\)/;s/(AM_INIT_AUTOMAKE.*)1\.7\.9/${1}1.7.6/' configure.in

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-server \
	--enable-client \
	%{?with_kerberos5:--with-gssapi} \
	--with-tmpdir=/tmp \
	--with-editor=/bin/vi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_cvs_root}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs

rm -f contrib/{.cvsignore,Makefile*,*.pl,*.sh,*.csh}
mv -f $RPM_BUILD_ROOT%{_datadir}/cvs/contrib/rcs2log $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre pserver
if [ -n "`/usr/bin/getgid cvs`" ]; then
	if [ "`/usr/bin/getgid cvs`" != "52" ]; then
		echo "Error: group cvs doesn't have gid=52. Correct this before installing cvs." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -f -g 52 cvs 1>&2
fi
if [ -n "`/bin/id -u cvs 2>/dev/null`" ]; then
	if [ "`/bin/id -u cvs`" != "52" ]; then
		echo "Error: user cvs doesn't have uid=52. Correct this before installing cvs." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g cvs -d %{_cvs_root} -u 52 -s /bin/false cvs 1>&2
fi

%post pserver
if [ "$1" = "1" ]; then
	# Initialise repository
	%{_bindir}/cvs -d :local:%{_cvs_root} init
	chown -R cvs:cvs %{_cvs_root}/CVSROOT
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pserver
if [ "$1" = "0" ]; then
	# Remove user and group
	/usr/sbin/userdel cvs 2>/dev/null
	/usr/sbin/groupdel cvs 2>/dev/null
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%files
%defattr(644,root,root,755)
%doc BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog doc/*.ps contrib
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[158]/*
%{_infodir}/cvs*

%files pserver
%defattr(644,root,root,755)
%attr(770,root,cvs) %dir %{_cvs_root}
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/cvs
