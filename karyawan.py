import pandas as pd
import os
import glob
import time
from colorama import Fore, init
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich import print as rprint

init(autoreset=True)
console = Console()

FOLDER_PATH = r'c:/Users/ASUS/baru/Desain2/'

class BacktrackingStrict:
    def __init__(self):
        self.hari_list = ['SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT']
        self.shift_info = {
            'SHIFT 1': {'jam': '08:00-16:00', 'color': 'cyan', 'ket': 'PAGI'},
            'SHIFT 2': {'jam': '16:00-00:00', 'color': 'yellow', 'ket': 'SORE'},
            'SHIFT 3': {'jam': '00:00-08:00', 'color': 'magenta', 'ket': 'MALAM'}
        }
        
        csv_files = glob.glob(os.path.join(FOLDER_PATH, "*.csv"))
        if not csv_files:
            raise FileNotFoundError("❌ File CSV tidak ditemukan!")
        
        self.active_file = csv_files[0]
        df = pd.read_csv(self.active_file, encoding='utf-8')
        df = df.dropna(how='all') 
        
        df['Jabatan'] = df['Jabatan'].fillna('Tidak Ada').astype(str).str.strip()
        df['Nama'] = df['Nama'].fillna('Tanpa Nama').astype(str).str.strip()
        
        self.pool = {
            'Admin': df[df['Jabatan'].str.contains('Admin', case=False, na=False)].to_dict('records'),
            'Teknisi': df[df['Jabatan'].str.contains('Teknisi', case=False, na=False)].to_dict('records'),
            'Kasir': df[df['Jabatan'].str.contains('Kasir', case=False, na=False)].to_dict('records')
        }

        self.jadwal_final = {}
        self.tracker_harian = {hari: set() for hari in self.hari_list}
        self.tracker_global_shift = {s_key: set() for s_key in self.shift_info.keys()}
        self.execution_time = 0

    def is_safe_strict(self, nama, hari, shift):
        if nama in self.tracker_harian[hari]: return False
        if nama in self.tracker_global_shift[shift]: return False
        return True

    def solve(self):
        start_time = time.perf_counter()
        pointers = {'Admin': 0, 'Teknisi': 0, 'Kasir': 0}
        
        # Simulasi progress bar modern
        for hari in track(self.hari_list, description="[bold green]Menyusun Jadwal..."):
            self.jadwal_final[hari] = {}
            for s_key in self.shift_info:
                self.jadwal_final[hari][s_key] = []
                for pos in range(1, 6):
                    row_assignment = {}
                    for jabatan in ['Admin', 'Teknisi', 'Kasir']:
                        kandidat_pool = self.pool[jabatan]
                        found = False
                        
                        for _ in range(len(kandidat_pool)):
                            kandidat = kandidat_pool[pointers[jabatan] % len(kandidat_pool)]
                            nama = kandidat['Nama']
                            if self.is_safe_strict(nama, hari, s_key):
                                row_assignment[jabatan] = nama
                                self.tracker_harian[hari].add(nama)
                                self.tracker_global_shift[s_key].add(nama)
                                pointers[jabatan] += 1
                                found = True
                                break
                            pointers[jabatan] += 1
                        
                        if not found:
                            for _ in range(len(kandidat_pool)):
                                kandidat = kandidat_pool[pointers[jabatan] % len(kandidat_pool)]
                                nama = kandidat['Nama']
                                if nama not in self.tracker_harian[hari]:
                                    row_assignment[jabatan] = f"[yellow]*{nama}[/yellow]"
                                    self.tracker_harian[hari].add(nama)
                                    pointers[jabatan] += 1
                                    found = True
                                    break
                                pointers[jabatan] += 1

                        if not found:
                            row_assignment[jabatan] = "[bold red]BENTROK[/bold red]"
                    
                    self.jadwal_final[hari][s_key].append(row_assignment)
        
        self.execution_time = time.perf_counter() - start_time

    def draw(self):
        rprint(Panel.fit("[bold white]MANPOWER DASHBOARD v10.0[/bold white]\n[dim]Backtracking Engine Active[/dim]", border_style="blue"))

        for hari in self.hari_list:
            table = Table(title=f"\n📅 JADWAL HARI: [bold cyan]{hari}[/bold cyan]", show_header=True, header_style="bold white", border_style="dim")
            
            table.add_column("SHIFT", width=15)
            table.add_column("JAM", width=12)
            table.add_column("POS", justify="center")
            table.add_column("ADMINISTRATOR", width=25)
            table.add_column("TECHNICIAN", width=25)
            table.add_column("CASHIER", width=25)

            for s_key, s_val in self.shift_info.items():
                for i, assignment in enumerate(self.jadwal_final[hari][s_key]):
                    is_first = (i == 0)
                    table.add_row(
                        f"[{s_val['color']}]{s_key if is_first else ''}[/]",
                        f"[dim]{s_val['jam'] if is_first else ''}[/]",
                        f"STA-{i+1:02d}",
                        assignment['Admin'],
                        assignment['Teknisi'],
                        assignment['Kasir'],
                        end_section=(i == 4)
                    )
            console.print(table)

        rprint(f"\n[bold green]📊 PERFORMA SISTEM:[/bold green]")
        rprint(f"⏱️  Waktu Eksekusi  : [yellow]{self.execution_time:.6f} Detik[/yellow]")

    def run_blackbox_test(self):
        table = Table(title="\n🛠️  INTEGRITY CHECK REPORT", border_style="yellow")
        table.add_column("Test Case", width=40)
        table.add_column("Status", justify="center")

        passed_all = True
        
        # 1. Test Keunikan Harian
        for hari in self.hari_list:
            names_in_day = []
            for s_key in self.shift_info:
                for slot in self.jadwal_final[hari][s_key]:
                    names_in_day.extend([slot['Admin'], slot['Teknisi'], slot['Kasir']])
            
            clean_names = [str(n).replace('[yellow]*', '').replace('[/yellow]', '') for n in names_in_day if "BENTROK" not in str(n)]
            if len(clean_names) != len(set(clean_names)):
                table.add_row(f"Keunikan Karyawan - {hari}", "[bold red]FAIL[/bold red]")
                passed_all = False
            else:
                table.add_row(f"Keunikan Karyawan - {hari}", "[bold green]PASS[/bold green]")

        console.print(table)
        status_msg = "[bold green]✅ SEMUA TEST BERHASIL[/bold green]" if passed_all else "[bold red]❌ TEST GAGAL[/bold red]"
        rprint(Panel(status_msg, expand=False))

if __name__ == "__main__":
    try:
        app = BacktrackingStrict()
        app.solve()
        app.draw()
        app.run_blackbox_test()
    except Exception as e:
        rprint(f"[bold red]ERROR:[/bold red] {e}")