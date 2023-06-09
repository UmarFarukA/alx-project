"""Added picture col to users

Revision ID: e9e93973e3af
Revises: 12be8a042851
Create Date: 2023-05-29 10:41:14.281065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9e93973e3af'
down_revision = '12be8a042851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('picture', sa.String(length=60), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('picture')

    # ### end Alembic commands ###
