# Generated by Django 3.2.6 on 2022-08-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0007_alter_inboxmessages_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileaccount',
            name='city',
            field=models.CharField(choices=[('Marrakech', 'Marrakech'), ('Fès', 'Fès'), ('Chefchaouen', 'Chefchaouen'), ('Essaouira', 'Essaouira'), ('Tanger', 'Tanger'), ('Casablanca', 'Casablanca'), ('Rabat', 'Rabat'), ('Meknès', 'Meknès'), ('Agadir', 'Agadir'), ('Ouarzazate', 'Ouarzazate'), ('Asilah', 'Asilah'), ('Tétouan', 'Tétouan'), ('Merzouga', 'Merzouga'), ('El Jadida', 'El Jadida'), ('Tinghir', 'Tinghir'), ('Ifrane', 'Ifrane'), ('Taroudant ', 'Taroudant'), ('Larache', 'Larache'), ('Aït Ben Haddou', 'Aït Ben Haddou'), ('Al Hoceïma', 'Al Hoceïma'), ('Oujda', 'Oujda'), ('Sidi Ifni', 'Sidi Ifni'), ('Azrou', 'Azrou'), ('Béni Mellal', 'Béni Mellal'), ('Midelt', 'Midelt'), ('Safi', 'Safi'), ('Taza', 'Taza'), ('Martil', 'Martil'), ('Oued Zem', 'Oued Zem'), ('Sefrou', 'Sefrou'), ('Taourirt', 'Taourirt'), ('Guercif', 'Guercif'), ('Tiflet', 'Tiflet'), ('Ouazzane', 'Ouazzane'), ('Youssoufia', 'Youssoufia'), ('Ksar El-Kébir', 'Ksar El-Kébir'), ('Fnideq', 'Fnideq'), ('Sidi Kacem', 'Sidi Kacem'), ('Saïdia', 'Saïdia'), ("M'diq", "M'diq"), ('Tiznit', 'Tiznit'), ('Moulay Idriss', 'Moulay Idriss'), ('Zerhoun', 'Zerhoun'), ('Guelmim', 'Guelmim'), ('Mohammédia', 'Mohammédia'), ('Imlil', 'Imlil'), ('Nador', 'Nador'), ('Berrchid', 'Berrchid'), ('Settat', 'Settat'), ('Berkane', 'Berkane')], default='Casablanca', max_length=50),
        ),
    ]
