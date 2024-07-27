from django.db import models

class RBC(models.Model):
  dimension = models.IntegerField()
  resolution = models.CharField(max_length=20)
  initial_condition = models.CharField(max_length=255,null = True)
  viscosity = models.FloatField()
  critical_rayleigh_number = models.FloatField()
  rayleigh_number = models.FloatField()
  prandtl_number = models.FloatField()
  thermal_diffusivity = models.FloatField()
  t_initial = models.FloatField()
  t_final = models.FloatField()
  path = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
    return "dim = " + str(self.dimension) + ", res = " + self.resolution + ", ic = " + self.initial_condition + ", vis = " + str(self.viscosity) + ", Ra = " + str(self.rayleigh_number) + ", Pr = " + str(self.prandtl_number) + ", t0 = " + str(self.t_initial) + ", tf = " + str(self.t_final) + ", path = " + self.path + ", desc = " + self.description

  def __getitem__(self, key):
    return getattr(self, key)

class Scalar(models.Model):
  dimension = models.IntegerField()
  resolution = models.CharField(max_length=20)
  initial_condition = models.CharField(max_length=255, null = True)
  viscosity = models.FloatField()
  critical_rayleigh_number = models.FloatField()
  rayleigh_number = models.FloatField()
  prandtl_number = models.FloatField()
  thermal_diffusivity = models.FloatField()
  t_initial = models.FloatField()
  t_final = models.FloatField()
  path = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self) -> str:
    return "dim = " + str(self.dimension) + ", res = " + self.resolution + ", ic = " + self.initial_condition + ", vis = " + str(self.viscosity) + ", Ra = " + str(self.rayleigh_number) + ", Pr = " + str(self.prandtl_number) + ", t0 = " + str(self.t_initial) + ", tf = " + str(self.t_final) + ", path = " + self.path + ", desc = " + self.description

  def __getitem__(self, key):
    return getattr(self, key)

class MHD(models.Model):
  dimension = models.IntegerField()
  resolution = models.CharField(max_length=20)
  initial_condition = models.CharField(max_length=255, null = True)
  viscosity = models.FloatField()
  magnetic_diffusivity = models.FloatField()
  t_initial = models.FloatField()
  t_final = models.FloatField()
  path = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self) -> str:
    return "dim = " + str(self.dimension) + ", res = " + self.resolution + ", ic = " + self.initial_condition + ", vis = " + str(self.viscosity) + ", mag = " + str(self.magnetic_diffusivity) + ", t0 = " + str(self.t_initial) + ", tf = " + str(self.t_final) + ", path = " + self.path + ", desc = " + self.description

  def __getitem__(self, key):
    return getattr(self, key)
  

class Hydro(models.Model):
  dimension = models.IntegerField()
  resolution = models.CharField(max_length=20)
  initial_condition = models.CharField(max_length=255, null = True)
  viscosity = models.FloatField()
  t_initial = models.FloatField()
  t_final = models.FloatField()
  path = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self) -> str:
    return "dim = " + str(self.dimension) + ", res = " + self.resolution + ", ic = " + self.initial_condition + ", vis = " + str(self.viscosity) + ", t0 = " + str(self.t_initial) + ", tf = " + str(self.t_final) + ", path = " + self.path + ", desc = " + self.description
  
  def __getitem__(self, key):
    return getattr(self, key)
  

class CompressibleConvection(models.Model):
  dimension = models.IntegerField()
  resolution = models.CharField(max_length=20)
  initial_condition = models.CharField(max_length=255, null = True)
  aspect_ratio = models.FloatField()
  epsilon = models.FloatField()
  dissipation_number = models.FloatField()
  gamma = models.FloatField()
  prandtl_number = models.FloatField()
  reyleigh_number = models.FloatField()
  t_initial = models.FloatField()
  t_final = models.FloatField()
  path = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self) -> str:
    return "dim = " + str(self.dimension) + ", res = " + self.resolution + ", ic = " + self.initial_condition +  ", t0 = " + str(self.t_initial) + ", tf = " + str(self.t_final) + ", path = " + self.path + ", desc = " + self.description
  
  def __getitem__(self, key):
    return getattr(self, key)
